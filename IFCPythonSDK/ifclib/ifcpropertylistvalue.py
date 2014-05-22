#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertyListValue.py
import log
import common
from ifcsimpleproperty import IFCSIMPLEPROPERTY

from utils import *

class IFCPROPERTYLISTVALUE(IFCSIMPLEPROPERTY):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYLISTVALUE,self).__init__(id,arg)
        self.type='IFCPROPERTYLISTVALUE'
        self.inverse={}
        self.ListValues=None #LIST
        self.Unit=None #IfcUnit


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYLISTVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYLISTVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ListValues= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Unit= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYLISTVALUE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPROPERTYLISTVALUE,self).toString()       
        line += listParamToSPF(self.ListValues,typerefToSPF)+','
        line += typerefToSPF(self.Unit)+','

        return line
