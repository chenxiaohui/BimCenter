#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertyTableValue.py
import log
import common
from ifcsimpleproperty import IFCSIMPLEPROPERTY

from utils import *

class IFCPROPERTYTABLEVALUE(IFCSIMPLEPROPERTY):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYTABLEVALUE,self).__init__(id,arg)
        self.type='IFCPROPERTYTABLEVALUE'
        self.inverse={}
        self.DefiningValues=None #LIST
        self.DefinedValues=None #LIST
        self.Expression=None #IfcText
        self.DefiningUnit=None #IfcUnit
        self.DefinedUnit=None #IfcUnit


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYTABLEVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYTABLEVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DefiningValues= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DefinedValues= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Expression= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DefiningUnit= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DefinedUnit= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYTABLEVALUE,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCPROPERTYTABLEVALUE,self).toString()       
        line += listParamToSPF(self.DefiningValues,typerefToSPF)+','
        line += listParamToSPF(self.DefinedValues,typerefToSPF)+','
        line += strToSPF(self.Expression)+','
        line += typerefToSPF(self.DefiningUnit)+','
        line += typerefToSPF(self.DefinedUnit)+','

        return line
