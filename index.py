#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on May 18, 2018, 5:14 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

# Create a Navigation page through flask®️
from flask import Flask, render_template, request, url_for, redirect
from model import ClassifyModel
from model import WebsiteModel
from spider import get_website_info
from spider import download_icon

app = Flask(__name__)


# Main Page
@app.route('/')
def index():
    websites = WebsiteModel.select().where(WebsiteModel.weight != 0)
    classifies = ClassifyModel.select().where(ClassifyModel.weight != 0).order_by(-ClassifyModel.weight)
    print(len(websites))
    dct = {
        "websites": websites,
        "classifies": classifies
    }
    return render_template("index.html", **dct)


# Administration
@app.route('/admin')
def admin():
    websites = (
        WebsiteModel.select()
            .join(ClassifyModel)
            .order_by(
            ClassifyModel.weight.desc(),
            WebsiteModel.weight.desc()
        )
    )

    return render_template('admin.html', websites=websites)


# Delete
@app.route('/delete')
def delete():
    uid = request.args.get('uid')
    WebsiteModel.delete().where(WebsiteModel.id == uid).execute()
    return redirect(url_for('admin'))


# Edit, adding, renew
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        uid = request.args.get('uid')
        website = WebsiteModel.select().where(WebsiteModel.id == uid).first()
        classifies = ClassifyModel.select()

        return render_template(
            "edit.html",
            website=website,
            classifies=classifies
        )

    elif request.method == 'POST':
        title = request.form.get('title', '')
        if title == '':
            return 'No empty Address!'

        url = request.form.get('url', '')
        if url == '':
            return 'No Empty Links!'

        ico = request.form.get('ico', '')
        print('ico', type(ico), ico)

        ret = None

        if ico == '':
            ret = get_website_info(url)
            ico = ret.get('icon')
        ico = download_icon(ico)

        description = request.form.get('description', '')
        if description == '':
            if ret == None:
                ret = get_website_info(url)
            description = ret.get('title', '')

        # None
        classify_id = request.form.get('classify', '')
        classify_id = int(classify_id) if classify_id != '' else 0

        print(classify_id, type(classify_id))

        weight = request.form.get('weight', '')
        weight = int(weight) if weight != '' else 1

        uid = request.form.get('uid', '')
        ret = WebsiteModel.select().where(WebsiteModel.id == uid).first() if uid != '' else None

        # if any updates existes
        if ret:
            print('Updating...')
            WebsiteModel.update(
                title=title,
                ico=ico,
                description=description,
                url=url,
                classify_id=classify_id,
                weight=weight
            ).where(WebsiteModel.id == uid).execute()

        else:
            # if the name is same
            ret = WebsiteModel.select().where(WebsiteModel.title == title)
            if len(ret) != 0:
                print('The website does exist.', title)
            else:
                WebsiteModel.create(
                    title=title,
                    ico=ico,
                    description=description,
                    url=url,
                    classify_id=classify_id,
                    weight=weight
                )
                print('Successfully Added.', title)

        return redirect(url_for('admin'))


# Editing the classifies
@app.route('/classify', methods=['GET', 'POST'])
def classify():
    if request.method == 'GET':
        classifies = ClassifyModel.select().order_by(ClassifyModel.weight.desc())
        return render_template('classify.html', classifies=classifies)
    elif request.method == 'POST':
        name = request.form.get('name', '')
        if name == '':
            return 'No empty'
        weight = request.form.get('weight', '1')
        ret = ClassifyModel.select().where(ClassifyModel.name == name)

        if len(ret) == 0:
            ClassifyModel.create(name=name, weight=weight)
        else:
            ClassifyModel.update(weight=weight).where(ClassifyModel.name == name).execute()

        return redirect(url_for('classify'))


# Delete Tags
@app.route('/delete-classify')
def delete_classify():
    uid = request.args.get('uid')
    classify = ClassifyModel.select().where(ClassifyModel.id == uid).first()

    if len(classify.websites) == 0:
        ClassifyModel.delete().where(ClassifyModel.id == uid).execute()
    else:
        print('Can not be deleted.')
    return redirect(url_for('classify'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
