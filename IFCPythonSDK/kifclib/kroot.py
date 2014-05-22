#!/usr/bin/python
#coding=utf-8
#Filename:KRoot.py
import log
import common
from baseobject import BaseObject
from utils import *

class KROOT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(KROOT,self).__init__(id,arg)
        self.type='KROOT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(KROOT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(KROOT,self).init():
            return False

        return True

    def getAttrCount(self):
        """"""
        return super(KROOT,self).getAttrCount()+0
