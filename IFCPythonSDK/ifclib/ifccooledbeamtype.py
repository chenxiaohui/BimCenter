#!/usr/bin/python
#coding=utf-8
#Filename:IfcCooledBeamType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCCOOLEDBEAMTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCOOLEDBEAMTYPE,self).__init__(id,arg)
        self.type='IFCCOOLEDBEAMTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcCooledBeamTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCOOLEDBEAMTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOOLEDBEAMTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOOLEDBEAMTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCOOLEDBEAMTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
