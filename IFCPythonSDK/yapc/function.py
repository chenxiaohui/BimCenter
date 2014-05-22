#!/usr/bin/python
#coding=utf-8
#Filename:function.py
from serializable import Serializable
class Function(Serializable):
    """"""
    def __init__(self):
        super(Function,self).__init__()
        self.arg={}
        self.ret={}
        self.local={}
        self.code=''
        
