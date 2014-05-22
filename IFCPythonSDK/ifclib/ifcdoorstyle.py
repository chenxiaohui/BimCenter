#!/usr/bin/python
#coding=utf-8
#Filename:IfcDoorStyle.py
import log
import common
from ifctypeproduct import IFCTYPEPRODUCT

from utils import *

class IFCDOORSTYLE(IFCTYPEPRODUCT):
    """"""
    def __init__(self,id,arg):
        super(IFCDOORSTYLE,self).__init__(id,arg)
        self.type='IFCDOORSTYLE'
        self.inverse={}
        self.OperationType=None #IfcDoorStyleOperationEnum
        self.ConstructionType=None #IfcDoorStyleConstructionEnum
        self.ParameterTakesPrecedence=None #BOOLEAN
        self.Sizeable=None #BOOLEAN


    def load(self):
        """register inverses"""
        if not super(IFCDOORSTYLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDOORSTYLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OperationType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConstructionType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ParameterTakesPrecedence= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Sizeable= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDOORSTYLE,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCDOORSTYLE,self).toString()       
        line += typerefToSPF(self.OperationType)+','
        line += typerefToSPF(self.ConstructionType)+','
        line += logicalToSPF(self.ParameterTakesPrecedence)+','
        line += logicalToSPF(self.Sizeable)+','

        return line
