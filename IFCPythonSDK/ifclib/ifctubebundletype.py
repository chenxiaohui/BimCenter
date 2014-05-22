#!/usr/bin/python
#coding=utf-8
#Filename:IfcTubeBundleType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCTUBEBUNDLETYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCTUBEBUNDLETYPE,self).__init__(id,arg)
        self.type='IFCTUBEBUNDLETYPE'
        self.inverse={}
        self.PredefinedType=None #IfcTubeBundleTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCTUBEBUNDLETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTUBEBUNDLETYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTUBEBUNDLETYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCTUBEBUNDLETYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
