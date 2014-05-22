#!/usr/bin/python
#coding=utf-8
#Filename:IfcHumidifierType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCHUMIDIFIERTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCHUMIDIFIERTYPE,self).__init__(id,arg)
        self.type='IFCHUMIDIFIERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcHumidifierTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCHUMIDIFIERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCHUMIDIFIERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCHUMIDIFIERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCHUMIDIFIERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
