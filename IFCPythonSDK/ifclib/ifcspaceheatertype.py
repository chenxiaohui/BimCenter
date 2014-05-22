#!/usr/bin/python
#coding=utf-8
#Filename:IfcSpaceHeaterType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCSPACEHEATERTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCSPACEHEATERTYPE,self).__init__(id,arg)
        self.type='IFCSPACEHEATERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcSpaceHeaterTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSPACEHEATERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSPACEHEATERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSPACEHEATERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSPACEHEATERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
