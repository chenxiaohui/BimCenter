#!/usr/bin/python
#coding=utf-8
#Filename:IfcChillerType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCCHILLERTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCHILLERTYPE,self).__init__(id,arg)
        self.type='IFCCHILLERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcChillerTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCHILLERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCHILLERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCHILLERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCHILLERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
