#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertyEnumeration.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPROPERTYENUMERATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYENUMERATION,self).__init__(id,arg)
        self.type='IFCPROPERTYENUMERATION'
        self.inverse={}
        self.Name=None #IfcLabel
        self.EnumerationValues=None #LIST
        self.Unit=None #IfcUnit


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYENUMERATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYENUMERATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EnumerationValues= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Unit= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYENUMERATION,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCPROPERTYENUMERATION,self).toString()       
        line += strToSPF(self.Name)+','
        line += listParamToSPF(self.EnumerationValues,typerefToSPF)+','
        line += typerefToSPF(self.Unit)+','

        return line
