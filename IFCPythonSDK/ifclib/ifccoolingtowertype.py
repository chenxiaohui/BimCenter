#!/usr/bin/python
#coding=utf-8
#Filename:IfcCoolingTowerType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCCOOLINGTOWERTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCOOLINGTOWERTYPE,self).__init__(id,arg)
        self.type='IFCCOOLINGTOWERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcCoolingTowerTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCOOLINGTOWERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOOLINGTOWERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOOLINGTOWERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCOOLINGTOWERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
