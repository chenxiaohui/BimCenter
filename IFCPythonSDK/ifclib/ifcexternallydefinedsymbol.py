#!/usr/bin/python
#coding=utf-8
#Filename:IfcExternallyDefinedSymbol.py
import log
import common
from ifcexternalreference import IFCEXTERNALREFERENCE

from utils import *

class IFCEXTERNALLYDEFINEDSYMBOL(IFCEXTERNALREFERENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCEXTERNALLYDEFINEDSYMBOL,self).__init__(id,arg)
        self.type='IFCEXTERNALLYDEFINEDSYMBOL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCEXTERNALLYDEFINEDSYMBOL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEXTERNALLYDEFINEDSYMBOL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEXTERNALLYDEFINEDSYMBOL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCEXTERNALLYDEFINEDSYMBOL,self).toString()       

        return line
