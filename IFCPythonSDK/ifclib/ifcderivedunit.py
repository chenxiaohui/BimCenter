#!/usr/bin/python
#coding=utf-8
#Filename:IfcDerivedUnit.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCDERIVEDUNIT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCDERIVEDUNIT,self).__init__(id,arg)
        self.type='IFCDERIVEDUNIT'
        self.inverse={}
        self.Elements=None #SET
        self.UnitType=None #IfcDerivedUnitEnum
        self.UserDefinedType=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCDERIVEDUNIT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDERIVEDUNIT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Elements= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UnitType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedType= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDERIVEDUNIT,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCDERIVEDUNIT,self).toString()       
        line += listParamToSPF(self.Elements,idToSPF)+','
        line += typerefToSPF(self.UnitType)+','
        line += strToSPF(self.UserDefinedType)+','

        return line
