#!/usr/bin/python
#coding=utf-8
#Filename:IfcDefinedSymbol.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCDEFINEDSYMBOL(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCDEFINEDSYMBOL,self).__init__(id,arg)
        self.type='IFCDEFINEDSYMBOL'
        self.inverse={}
        self.Definition=None #IfcDefinedSymbolSelect
        self.Target=None #IfcCartesianTransformationOperator2D


    def load(self):
        """register inverses"""
        if not super(IFCDEFINEDSYMBOL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDEFINEDSYMBOL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Definition= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Target= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDEFINEDSYMBOL,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCDEFINEDSYMBOL,self).toString()       
        line += typerefToSPF(self.Definition)+','
        line += idToSPF(self.Target)+','

        return line
