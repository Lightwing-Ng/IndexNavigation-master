# IndexNavigation-master
## 致谢
fork从彭世瑜先生的GitHub项目：
```
https://github.com/mouday/index_falsk
```
## Directory Structure
```
.
├── .DS_Store
├── .git
│   ├── HEAD
│   ├── branches
│   ├── config
│   ├── description
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   └── update.sample
│   ├── info
│   │   └── exclude
│   ├── objects
│   │   ├── info
│   │   └── pack
│   └── refs
│       ├── heads
│       └── tags
├── .idea
│   ├── index_falsk.iml
│   ├── inspectionProfiles
│   │   └── profiles_settings.xml
│   ├── misc.xml
│   ├── modules.xml
│   └── workspace.xml
├── README.md
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-36.pyc
│   ├── app.cpython-36.pyc
│   ├── index.cpython-36.pyc
│   ├── model.cpython-36.pyc
│   └── spider.cpython-36.pyc
├── app.py
├── index.py
├── model.py
├── requirements.txt
├── spider.py
├── static
│   ├── .DS_Store
│   ├── bootstrap-3.3.7-dist
│   │   ├── css
│   │   │   ├── bootstrap-theme.css
│   │   │   ├── bootstrap-theme.css.map
│   │   │   ├── bootstrap-theme.min.css
│   │   │   ├── bootstrap-theme.min.css.map
│   │   │   ├── bootstrap.css
│   │   │   ├── bootstrap.css.map
│   │   │   ├── bootstrap.min.css
│   │   │   └── bootstrap.min.css.map
│   │   ├── fonts
│   │   │   ├── Microsoft\ YaHei\ UI\ Light.ttf
│   │   │   ├── glyphicons-halflings-regular.eot
│   │   │   ├── glyphicons-halflings-regular.svg
│   │   │   ├── glyphicons-halflings-regular.ttf
│   │   │   ├── glyphicons-halflings-regular.woff
│   │   │   └── glyphicons-halflings-regular.woff2
│   │   └── js
│   │       ├── bootstrap.js
│   │       ├── bootstrap.min.js
│   │       └── npm.js
│   ├── css
│   │   └── index.css
│   ├── ico
│   │   ├── 12306.cn.ico
│   │   ├── 2345.com.ico
│   │   ├── 315online.com.ico
│   │   ├── 360.cn.ico
│   │   ├── 36kr.com.ico
│   │   ├── 51aistar.com.png
│   │   ├── 51zxw.net.ico
│   │   ├── 8.url.cn.ico
│   │   ├── admin5.com.ico
│   │   ├── adtchrome.com.ico
│   │   ├── alexa.com.ico
│   │   ├── alipay.com.ico
│   │   ├── anaconda.com.ico
│   │   ├── app.gomein.net.cn.ico
│   │   ├── apple.com.ico
│   │   ├── baidu.com.ico
│   │   ├── baifubao.com.ico
│   │   ├── bbc.com.ico
│   │   ├── beautifulsoup.readthedocs.io.ico
│   │   ├── biz.jrj.com.cn.ico
│   │   ├── bj.96weixin.com.ico
│   │   ├── bjgjj.gov.cn.ico
│   │   ├── bjrbj.gov.cn.ico
│   │   ├── blog.sina.com.cn.ico
│   │   ├── c.open.163.com.ico
│   │   ├── cdn.itjuzi.com.ico
│   │   ├── cdn.kmplayer.com.ico
│   │   ├── cdn.sstatic.net.ico
│   │   ├── cdn2.jianshu.io.ico
│   │   ├── cfan.com.cn.ico
│   │   ├── chinaipo.com.ico
│   │   ├── cmbchina.com.ico
│   │   ├── cn.bing.com.ico
│   │   ├── cn.udacity.com.ico
│   │   ├── common.cnblogs.com.ico
│   │   ├── coursera.org.ico
│   │   ├── crummy.com.ico
│   │   ├── csdnimg.cn.ico
│   │   ├── css.doyoe.com.ico
│   │   ├── dangdang.com.ico
│   │   ├── dayqkl.com.ico
│   │   ├── developer.apple.com.ico
│   │   ├── developers.google.cn.png
│   │   ├── discuz.net.ico
│   │   ├── dl.xunlei.com.ico
│   │   ├── dn-coding-net-production-static.qbox.me.ico
│   │   ├── docs.djangoproject.com.ico
│   │   ├── douyu.com.ico
│   │   ├── dt.datadang.com.ico
│   │   ├── eclipse.org.ico
│   │   ├── edu-image.nosdn.127.net.png
│   │   ├── edu.51cto.com.ico
│   │   ├── edu.aliyun.com.ico
│   │   ├── edu.csdn.net.ico
│   │   ├── fakenamegenerator.com.ico
│   │   ├── fanyi.bdstatic.com.ico
│   │   ├── farthe.com.ico
│   │   ├── foxmail.com.ico
│   │   ├── gallery.cache.wps.cn.ico
│   │   ├── github.com.ico
│   │   ├── google.cn.ico
│   │   ├── hackdesign.org.ico
│   │   ├── hao.360.cn.ico
│   │   ├── hao123.com.ico
│   │   ├── hostinger.com.hk.ico
│   │   ├── htmldog.com.ico
│   │   ├── huya.com.ico
│   │   ├── i.h2.pdim.gs.ico
│   │   ├── i.mi.com.ico
│   │   ├── icbc.com.cn.ico
│   │   ├── iciba.com.ico
│   │   ├── icloud.com.ico
│   │   ├── icourses.cn.ico
│   │   ├── img.ucdl.pp.uc.cn.ico
│   │   ├── img.weiyun.com.ico
│   │   ├── img00.zhaopin.cn.ico
│   │   ├── imooc.com.ico
│   │   ├── ithome.com.ico
│   │   ├── ituring.com.cn.png
│   │   ├── jd.com.ico
│   │   ├── jekyll.com.cn.ico
│   │   ├── jetbrains.com.ico
│   │   ├── jquery.cuishifeng.cn.ico
│   │   ├── json.cn.ico
│   │   ├── lagou.com.ico
│   │   ├── leetcode.com.ico
│   │   ├── liaoxuefeng.com.ico
│   │   ├── m.baidu.com.png
│   │   ├── mail.163.com.ico
│   │   ├── mail.qq.com.ico
│   │   ├── mat1.gtimg.com.ico
│   │   ├── mooc.cn.ico
│   │   ├── mouday.com.ico
│   │   ├── msdn.itellyou.cn.ico
│   │   ├── msdn.microsoft.com.ico
│   │   ├── mva.microsoft.com.ico
│   │   ├── naotu.baidu.com.ico
│   │   ├── neea.edu.cn.ico
│   │   ├── nfil.es.ico
│   │   ├── note.youdao.com.ico
│   │   ├── npm.taobao.org.png
│   │   ├── open.vipexam.org.ico
│   │   ├── openlivewriter.org.ico
│   │   ├── oracle.com.ico
│   │   ├── oreilly.com.cn.ico
│   │   ├── oschina.net.ico
│   │   ├── pc1.gtimg.com.ico
│   │   ├── pconline.com.cn.ico
│   │   ├── pengshiyu.com.ico
│   │   ├── pro.qimingpian.com.ico
│   │   ├── processon.com.ico
│   │   ├── prodev.qimingpian.com.ico
│   │   ├── pupong.com.ico
│   │   ├── pyinstaller.org.ico
│   │   ├── pythontutor.com.ico
│   │   ├── qimingpian.com.ico
│   │   ├── qiyipic.com.ico
│   │   ├── rarlab.com.ico
│   │   ├── regex101.com.ico
│   │   ├── regexr.com.ico
│   │   ├── res.wx.qq.com.ico
│   │   ├── resource.jinse.com.ico
│   │   ├── s01.mifile.cn.ico
│   │   ├── s1.music.126.net.ico
│   │   ├── scrapy-chs.readthedocs.io.ico
│   │   ├── selenium-python-docs-zh.readthedocs.io.ico
│   │   ├── shouzhi.net.cn.ico
│   │   ├── splayer.org.ico
│   │   ├── sputniknews.cn.ico
│   │   ├── sta.36krcnd.com.ico
│   │   ├── static.bootcss.com.png
│   │   ├── static.clewm.net.ico
│   │   ├── static.freebuf.com.ico
│   │   ├── static.hdslb.com.ico
│   │   ├── static.quanmin.tv.ico
│   │   ├── static.runoob.com.ico
│   │   ├── static.segmentfault.com.ico
│   │   ├── static.shiyanlou.com.ico
│   │   ├── static.yunaq.com.ico
│   │   ├── study.163.com.ico
│   │   ├── taobao.com.ico
│   │   ├── tech.datadang.com.ico
│   │   ├── tiobe.com.ico
│   │   ├── top500.org.ico
│   │   ├── ultraedit.com.ico
│   │   ├── vip.qimingpian.com.ico
│   │   ├── weibo.com.ico
│   │   ├── weirenwu.weibo.com.ico
│   │   ├── who.is.ico
│   │   ├── wholetomato.com.ico
│   │   ├── wxeditor.com.ico
│   │   ├── xiaomi.com.ico
│   │   ├── xigua.com.ico
│   │   ├── youku.com.ico
│   │   ├── yq.aliyun.com.ico
│   │   ├── yun.baidu.com.ico
│   │   ├── zentao.qimingpian.com.ico
│   │   └── zhanqi.tv.ico
│   └── images
│       ├── .DS_Store
│       ├── baidu.png
│       └── favicon.ico
├── templates
│   ├── admin.html
│   ├── classify.html
│   ├── edit.html
│   └── index.html
└── webdata.db
```
## 功能
实现爬虫并生成导航首页
## 运行
+ 安装依赖包
```
$pip install -r requirements.txt
```
+ 运行
```
$python3 index.py
```