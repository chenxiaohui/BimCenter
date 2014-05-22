#!/usr/bin/python
#coding=utf-8
#Filename:BaseObject.py
from serializable import Serializable

class BaseObject(Serializable):
    """"""
    def __init__(self,id,data):
        super(BaseObject,self).__init__()
        self.lid=id
        self.args=data    
        self.binited=False
        self.expDataSet=None 
        self.type=''
        
    def inited(self):
        """"""
        if not self.binited:
            self.binited=True
            if self.init():
                del self.args
        return self.binited

    def load(self):
        """"""
        return True

    def init(self):
        """"""
        return True
        
    def getAttrCount(self):
        """"""
        return 0

    def toString(self):
        """"""
        return ''

