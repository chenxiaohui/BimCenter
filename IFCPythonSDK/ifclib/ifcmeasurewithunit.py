#!/usr/bin/python
#coding=utf-8
#Filename:IfcMeasureWithUnit.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCMEASUREWITHUNIT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCMEASUREWITHUNIT,self).__init__(id,arg)
        self.type='IFCMEASUREWITHUNIT'
        self.inverse={}
        self.ValueComponent=None #IfcValue
        self.UnitComponent=None #IfcUnit


    def load(self):
        """register inverses"""
        if not super(IFCMEASUREWITHUNIT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMEASUREWITHUNIT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ValueComponent= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UnitComponent= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMEASUREWITHUNIT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCMEASUREWITHUNIT,self).toString()       
        line += typerefToSPF(self.ValueComponent)+','
        line += typerefToSPF(self.UnitComponent)+','

        return line
