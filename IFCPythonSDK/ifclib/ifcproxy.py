#!/usr/bin/python
#coding=utf-8
#Filename:IfcProxy.py
import log
import common
from ifcproduct import IFCPRODUCT

from utils import *

class IFCPROXY(IFCPRODUCT):
    """"""
    def __init__(self,id,arg):
        super(IFCPROXY,self).__init__(id,arg)
        self.type='IFCPROXY'
        self.inverse={}
        self.ProxyType=None #IfcObjectTypeEnum
        self.Tag=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCPROXY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROXY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProxyType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Tag= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROXY,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPROXY,self).toString()       
        line += typerefToSPF(self.ProxyType)+','
        line += strToSPF(self.Tag)+','

        return line
