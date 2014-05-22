#!/usr/bin/python
#coding=utf-8
#Filename:IfcLampType.py
import log
import common
from ifcflowterminaltype import IFCFLOWTERMINALTYPE

from utils import *

class IFCLAMPTYPE(IFCFLOWTERMINALTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCLAMPTYPE,self).__init__(id,arg)
        self.type='IFCLAMPTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcLampTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCLAMPTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLAMPTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLAMPTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCLAMPTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
