#!/usr/bin/python
#coding=utf-8
#Filename:IfcCondenserType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCCONDENSERTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCONDENSERTYPE,self).__init__(id,arg)
        self.type='IFCCONDENSERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcCondenserTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCONDENSERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONDENSERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONDENSERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCONDENSERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
