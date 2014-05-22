#!/usr/bin/python
#coding=utf-8
#Filename:IfcElementQuantity.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCELEMENTQUANTITY(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCELEMENTQUANTITY,self).__init__(id,arg)
        self.type='IFCELEMENTQUANTITY'
        self.inverse={}
        self.MethodOfMeasurement=None #IfcLabel
        self.Quantities=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCELEMENTQUANTITY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELEMENTQUANTITY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MethodOfMeasurement= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Quantities= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELEMENTQUANTITY,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCELEMENTQUANTITY,self).toString()       
        line += strToSPF(self.MethodOfMeasurement)+','
        line += listParamToSPF(self.Quantities,idToSPF)+','

        return line
