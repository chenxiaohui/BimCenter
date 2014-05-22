#!/usr/bin/python
#coding=utf-8
#Filename:IfcWindowStyle.py
import log
import common
from ifctypeproduct import IFCTYPEPRODUCT

from utils import *

class IFCWINDOWSTYLE(IFCTYPEPRODUCT):
    """"""
    def __init__(self,id,arg):
        super(IFCWINDOWSTYLE,self).__init__(id,arg)
        self.type='IFCWINDOWSTYLE'
        self.inverse={}
        self.ConstructionType=None #IfcWindowStyleConstructionEnum
        self.OperationType=None #IfcWindowStyleOperationEnum
        self.ParameterTakesPrecedence=None #BOOLEAN
        self.Sizeable=None #BOOLEAN


    def load(self):
        """register inverses"""
        if not super(IFCWINDOWSTYLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWINDOWSTYLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConstructionType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OperationType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ParameterTakesPrecedence= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Sizeable= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCWINDOWSTYLE,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCWINDOWSTYLE,self).toString()       
        line += typerefToSPF(self.ConstructionType)+','
        line += typerefToSPF(self.OperationType)+','
        line += logicalToSPF(self.ParameterTakesPrecedence)+','
        line += logicalToSPF(self.Sizeable)+','

        return line
