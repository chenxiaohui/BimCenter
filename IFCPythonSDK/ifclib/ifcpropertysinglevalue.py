#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertySingleValue.py
import log
import common
from ifcsimpleproperty import IFCSIMPLEPROPERTY

from utils import *

class IFCPROPERTYSINGLEVALUE(IFCSIMPLEPROPERTY):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYSINGLEVALUE,self).__init__(id,arg)
        self.type='IFCPROPERTYSINGLEVALUE'
        self.inverse={}
        self.NominalValue=None #IfcValue
        self.Unit=None #IfcUnit


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYSINGLEVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYSINGLEVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.NominalValue= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Unit= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYSINGLEVALUE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPROPERTYSINGLEVALUE,self).toString()       
        line += typerefToSPF(self.NominalValue)+','
        line += typerefToSPF(self.Unit)+','

        return line
