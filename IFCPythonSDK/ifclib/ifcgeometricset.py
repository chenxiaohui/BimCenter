#!/usr/bin/python
#coding=utf-8
#Filename:IfcGeometricSet.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCGEOMETRICSET(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCGEOMETRICSET,self).__init__(id,arg)
        self.type='IFCGEOMETRICSET'
        self.inverse={}
        self.Elements=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCGEOMETRICSET,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGEOMETRICSET,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Elements= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGEOMETRICSET,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCGEOMETRICSET,self).toString()       
        line += listParamToSPF(self.Elements,typerefToSPF)+','

        return line
