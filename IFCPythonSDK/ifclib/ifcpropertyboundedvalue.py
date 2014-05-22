#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertyBoundedValue.py
import log
import common
from ifcsimpleproperty import IFCSIMPLEPROPERTY

from utils import *

class IFCPROPERTYBOUNDEDVALUE(IFCSIMPLEPROPERTY):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYBOUNDEDVALUE,self).__init__(id,arg)
        self.type='IFCPROPERTYBOUNDEDVALUE'
        self.inverse={}
        self.UpperBoundValue=None #IfcValue
        self.LowerBoundValue=None #IfcValue
        self.Unit=None #IfcUnit


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYBOUNDEDVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYBOUNDEDVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UpperBoundValue= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LowerBoundValue= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Unit= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYBOUNDEDVALUE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCPROPERTYBOUNDEDVALUE,self).toString()       
        line += typerefToSPF(self.UpperBoundValue)+','
        line += typerefToSPF(self.LowerBoundValue)+','
        line += typerefToSPF(self.Unit)+','

        return line
