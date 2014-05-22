#!/usr/bin/python
#coding=utf-8
#Filename:IfcNamedUnit.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCNAMEDUNIT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCNAMEDUNIT,self).__init__(id,arg)
        self.type='IFCNAMEDUNIT'
        self.inverse={}
        self.Dimensions=None #IfcDimensionalExponents
        self.UnitType=None #IfcUnitEnum


    def load(self):
        """register inverses"""
        if not super(IFCNAMEDUNIT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCNAMEDUNIT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Dimensions= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UnitType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCNAMEDUNIT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCNAMEDUNIT,self).toString()       
        line += idToSPF(self.Dimensions)+','
        line += typerefToSPF(self.UnitType)+','

        return line
