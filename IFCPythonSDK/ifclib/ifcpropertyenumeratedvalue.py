#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertyEnumeratedValue.py
import log
import common
from ifcsimpleproperty import IFCSIMPLEPROPERTY

from utils import *

class IFCPROPERTYENUMERATEDVALUE(IFCSIMPLEPROPERTY):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYENUMERATEDVALUE,self).__init__(id,arg)
        self.type='IFCPROPERTYENUMERATEDVALUE'
        self.inverse={}
        self.EnumerationValues=None #LIST
        self.EnumerationReference=None #IfcPropertyEnumeration


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYENUMERATEDVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYENUMERATEDVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EnumerationValues= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EnumerationReference= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYENUMERATEDVALUE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPROPERTYENUMERATEDVALUE,self).toString()       
        line += listParamToSPF(self.EnumerationValues,typerefToSPF)+','
        line += idToSPF(self.EnumerationReference)+','

        return line
