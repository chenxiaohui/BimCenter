#!/usr/bin/python
#coding=utf-8
#Filename:IfcCoilType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCCOILTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCOILTYPE,self).__init__(id,arg)
        self.type='IFCCOILTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcCoilTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCOILTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOILTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOILTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCOILTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line