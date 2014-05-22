#!/usr/bin/python
#coding=utf-8
#Filename:IfcTransformerType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCTRANSFORMERTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCTRANSFORMERTYPE,self).__init__(id,arg)
        self.type='IFCTRANSFORMERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcTransformerTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCTRANSFORMERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTRANSFORMERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTRANSFORMERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCTRANSFORMERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
