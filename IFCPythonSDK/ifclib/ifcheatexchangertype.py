#!/usr/bin/python
#coding=utf-8
#Filename:IfcHeatExchangerType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCHEATEXCHANGERTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCHEATEXCHANGERTYPE,self).__init__(id,arg)
        self.type='IFCHEATEXCHANGERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcHeatExchangerTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCHEATEXCHANGERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCHEATEXCHANGERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCHEATEXCHANGERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCHEATEXCHANGERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
