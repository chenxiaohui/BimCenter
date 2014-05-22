#!/usr/bin/python
#coding=utf-8
#Filename:IfcEvaporativeCoolerType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCEVAPORATIVECOOLERTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCEVAPORATIVECOOLERTYPE,self).__init__(id,arg)
        self.type='IFCEVAPORATIVECOOLERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcEvaporativeCoolerTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCEVAPORATIVECOOLERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEVAPORATIVECOOLERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEVAPORATIVECOOLERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCEVAPORATIVECOOLERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
