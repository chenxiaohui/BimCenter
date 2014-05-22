#!/usr/bin/python
#coding=utf-8
#Filename:IfcTankType.py
import log
import common
from ifcflowstoragedevicetype import IFCFLOWSTORAGEDEVICETYPE

from utils import *

class IFCTANKTYPE(IFCFLOWSTORAGEDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCTANKTYPE,self).__init__(id,arg)
        self.type='IFCTANKTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcTankTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCTANKTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTANKTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTANKTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCTANKTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
