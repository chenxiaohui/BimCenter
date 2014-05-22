#!/usr/bin/python
#coding=utf-8
#Filename:IfcBooleanResult.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCBOOLEANRESULT(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCBOOLEANRESULT,self).__init__(id,arg)
        self.type='IFCBOOLEANRESULT'
        self.inverse={}
        self.Operator=None #IfcBooleanOperator
        self.FirstOperand=None #IfcBooleanOperand
        self.SecondOperand=None #IfcBooleanOperand


    def load(self):
        """register inverses"""
        if not super(IFCBOOLEANRESULT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBOOLEANRESULT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Operator= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FirstOperand= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SecondOperand= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBOOLEANRESULT,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCBOOLEANRESULT,self).toString()       
        line += typerefToSPF(self.Operator)+','
        line += typerefToSPF(self.FirstOperand)+','
        line += typerefToSPF(self.SecondOperand)+','

        return line
