#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * email: rodney_ng@iCloud.com
 * created on May 18, 2018, 5:14 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import requests
from requests.exceptions import Timeout, MissingSchema
from requests.exceptions import ConnectionError
from lxml.etree import ParserError
from urllib.parse import urljoin, urlparse
from pyquery import PyQuery
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': 'gzip, deflate, br',
    "Accept-Language": "zh-CN,zh;q=0.9",
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive'
}


# to get the info of a website
def get_website_info(url):
    print('get_website_info-url: ', url)
    # default icon link
    result = urlparse(url)
    default_icon = urljoin(result.sheme + '://' + result.netloc, 'favicon.ico')
    print('default-ico: ', default_icon)

    title, icon = '', ''

    try:
        response = requests.get(url, headers=headers, timeout=3)
        print(response)
    except Timeout as e:
        pass
    except ConnectionError as e:
        pass
    else:
        response.encoding = response.apparent_encoding
        try:
            doc = PyQuery(response.text)
            title = doc('title').text().strip()
            icon = doc('link[rel="shortcut icon"]').attr('href')
            if icon == None:
                icon = doc('link[rel="SHORTCUT ICON"]').attr('href')
            print('parse-ico', icon)
        except ParserError:
            print('Document is empty')
            pass

        if icon == None or icon == '':
            icon = default_icon

        if icon.startswith('//'):
            icon = 'http:' + icon
        if not icon.startswith('http'):
            icon = urljoin(url, icon)

        print('get_website_info-icon: ', icon)
        print('get_website_info-title: ', title)

    dct = {
        'title': title,
        'icon': icon
    }
    print(dct)

    return dct


# Download icons
def download_icon(url):
    dirname = os.path.join('static', 'ico')
    savedir = os.path.join(BASE_DIR, dirname)

    # testing if the path is available
    test_path = os.path.join(BASE_DIR, url)
    print('test_path: ', test_path)

    # if it does exist, no need to download
    if os.path.isfile(test_path) and os.path.exists(test_path):
        return url

    print('url: ', url)

    # default icon
    icon_path = 'static/images/favicon.ico'

    # the path to save icons
    result = urlparse(url)
    print(result)
    ext = os.path.splitext(result.path)[-1]
    print(ext)
    domain = result.netloc.replace('www', '')
    file = domain + ext  # filename
    filename = os.path.join(dirname, file)
    fullname = os.path.join(savedir, file)

    # starting to download imgs
    try:
        response = requests.get(url, headers=headers, timeout=3)
        print(response)
    except Timeout as e:
        print('Download Timeout: ', url)
    except ConnectionError as e:
        print('Error with links: ', url)
    except MissingSchema:
        print('Schema Error: ', url)
    else:
        if response.status_code == 200:
            # Create the path if it does not exist
            if not os.path.isdir(savedir):
                os.mkdirs(savedir)

            with open(fullname, 'wb') as f:
                f.write(response.content)

            print(filename)
            icon_path = filename

    return icon_path


def move_tag():
    '''
    migrate data from websites
    :return:
    '''
    url = 'https://www.pengshiyu.com/hao.html'
    response = requests.get(url)
    print(response)
    doc = PyQuery(response.text)
    a_all = doc('a')

    count = 0
    for a in a_all.items():
        title = a.text()
        url = a.attr('href')
        if url.startswith('#'):
            continue
        data = {
            'title': title,
            'url': url,
            'classify': 1,
            'uid': '',
            'ico': '',
            'description': '',
            'weight': ''
        }
        print(data)
        count += 1
        ret = requests.post('http://127.0.0.1:5000/edit', data=data)
        print(ret)
    print('count: ', count)


if __name__ == '__main__':
    move_tag()
