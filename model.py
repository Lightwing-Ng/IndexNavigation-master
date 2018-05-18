#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on May 18, 2018, 5:14 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

from peewee import *
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_name = 'webdata.db'
db_path = os.path.join(BASE_DIR, db_name)
db = SqliteDatabase(db_path)


class BaseModel(Model):
    class Meta:
        database = db


# Classify
class ClassifyModel(BaseModel):
    name = CharField(null=True)
    weight = IntegerField(default=1)

    # spare
    flag = IntegerField(default=0)
    info = CharField(default='')


# Websites Name List
class WebsiteModel(BaseModel):
    title = CharField(null=False)
    ico = CharField(null=False)
    description = CharField(default='')
    url = CharField(null=True)

    # To classify the websites
    classify = ForeignKeyField(model=ClassifyModel, backref="websites", default=1)
    weight = IntegerField(default=1)

    # spare
    flag = IntegerField(default=0)
    info = CharField(default='')


tables = [ClassifyModel, WebsiteModel]
db.connect()
db.create_tables(tables, safe=True)
db.close()

if __name__ == '__main__':
    print(db_path)
