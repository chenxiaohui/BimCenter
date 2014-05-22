#!/usr/bin/python
#coding=utf-8
#Filename:IfcConversionBasedUnit.py
import log
import common
from ifcnamedunit import IFCNAMEDUNIT

from utils import *

class IFCCONVERSIONBASEDUNIT(IFCNAMEDUNIT):
    """"""
    def __init__(self,id,arg):
        super(IFCCONVERSIONBASEDUNIT,self).__init__(id,arg)
        self.type='IFCCONVERSIONBASEDUNIT'
        self.inverse={}
        self.Name=None #IfcLabel
        self.ConversionFactor=None #IfcMeasureWithUnit


    def load(self):
        """register inverses"""
        if not super(IFCCONVERSIONBASEDUNIT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONVERSIONBASEDUNIT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConversionFactor= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONVERSIONBASEDUNIT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCONVERSIONBASEDUNIT,self).toString()       
        line += strToSPF(self.Name)+','
        line += idToSPF(self.ConversionFactor)+','

        return line
