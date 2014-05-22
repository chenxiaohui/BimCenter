#!/usr/bin/python
#coding=utf-8
#Filename:IfcElectricGeneratorType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCELECTRICGENERATORTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCELECTRICGENERATORTYPE,self).__init__(id,arg)
        self.type='IFCELECTRICGENERATORTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcElectricGeneratorTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCELECTRICGENERATORTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELECTRICGENERATORTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELECTRICGENERATORTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCELECTRICGENERATORTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
