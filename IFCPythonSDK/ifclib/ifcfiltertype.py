#!/usr/bin/python
#coding=utf-8
#Filename:IfcFilterType.py
import log
import common
from ifcflowtreatmentdevicetype import IFCFLOWTREATMENTDEVICETYPE

from utils import *

class IFCFILTERTYPE(IFCFLOWTREATMENTDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFILTERTYPE,self).__init__(id,arg)
        self.type='IFCFILTERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcFilterTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCFILTERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFILTERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFILTERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFILTERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
