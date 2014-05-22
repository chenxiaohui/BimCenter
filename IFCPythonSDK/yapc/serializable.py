#!/usr/bin/python
#coding=utf-8
#Filename:Serializable.py
import json
class Serializable(object):
    """"""
    def __init__(self):
        super(Serializable,self).__init__()

    def Serialize(self):
        """"""
        return json.dumps(self.__dict__,indent=4)



