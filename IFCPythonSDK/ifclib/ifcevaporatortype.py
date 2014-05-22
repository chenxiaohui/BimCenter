#!/usr/bin/python
#coding=utf-8
#Filename:IfcEvaporatorType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCEVAPORATORTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCEVAPORATORTYPE,self).__init__(id,arg)
        self.type='IFCEVAPORATORTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcEvaporatorTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCEVAPORATORTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEVAPORATORTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEVAPORATORTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCEVAPORATORTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
