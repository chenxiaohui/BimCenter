#!/usr/bin/python
#coding=utf-8
#Filename:IfcServiceLifeFactor.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCSERVICELIFEFACTOR(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCSERVICELIFEFACTOR,self).__init__(id,arg)
        self.type='IFCSERVICELIFEFACTOR'
        self.inverse={}
        self.PredefinedType=None #IfcServiceLifeFactorTypeEnum
        self.UpperValue=None #IfcMeasureValue
        self.MostUsedValue=None #IfcMeasureValue
        self.LowerValue=None #IfcMeasureValue


    def load(self):
        """register inverses"""
        if not super(IFCSERVICELIFEFACTOR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSERVICELIFEFACTOR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UpperValue= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MostUsedValue= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LowerValue= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSERVICELIFEFACTOR,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCSERVICELIFEFACTOR,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','
        line += typerefToSPF(self.UpperValue)+','
        line += typerefToSPF(self.MostUsedValue)+','
        line += typerefToSPF(self.LowerValue)+','

        return line
