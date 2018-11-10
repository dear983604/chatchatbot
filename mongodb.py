# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 00:11:54 2018

@author: linzino
"""

from pymongo import MongoClient
import pymongo
import urllib.parse
from datetime import datetime 



# db setting
host = 'ds157853.mlab.com'
port = '57853'
username = urllib.parse.quote_plus('chatbotdb')
password = urllib.parse.quote_plus('YoWei19870507')
# Authentication Database
Authdb='chatbotdb'


def init_db():
    client = MongoClient('mongodb://%s:%s@%s:%s/%s?authMechanism=SCRAM-SHA-1'
                      % (username, password, host, port, Authdb))

    db = client[Authdb]
    return db


def insert_one(dic,collection):
    #collection_name = 'users'
    db = init_db()
    coll = db[collection]
    coll.insert_one(dic)


def get_all(collection):
    db = init_db()
    coll = db[collection]
    return list(coll.find())

def find_user(userid,collection):
    '''
    確認這個使用者是不是加入了
    '''
    db = init_db()
    coll = db[collection]
    return len(list(coll.find({"userid":userid})))



