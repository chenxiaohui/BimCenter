#!/usr/bin/python
#coding=utf-8
#Filename:IfcBoilerType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCBOILERTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCBOILERTYPE,self).__init__(id,arg)
        self.type='IFCBOILERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcBoilerTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCBOILERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBOILERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBOILERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCBOILERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
