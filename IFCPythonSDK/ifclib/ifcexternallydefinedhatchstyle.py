#!/usr/bin/python
#coding=utf-8
#Filename:IfcExternallyDefinedHatchStyle.py
import log
import common
from ifcexternalreference import IFCEXTERNALREFERENCE

from utils import *

class IFCEXTERNALLYDEFINEDHATCHSTYLE(IFCEXTERNALREFERENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCEXTERNALLYDEFINEDHATCHSTYLE,self).__init__(id,arg)
        self.type='IFCEXTERNALLYDEFINEDHATCHSTYLE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCEXTERNALLYDEFINEDHATCHSTYLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEXTERNALLYDEFINEDHATCHSTYLE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEXTERNALLYDEFINEDHATCHSTYLE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCEXTERNALLYDEFINEDHATCHSTYLE,self).toString()       

        return line
