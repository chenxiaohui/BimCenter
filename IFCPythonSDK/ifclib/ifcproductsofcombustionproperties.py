#!/usr/bin/python
#coding=utf-8
#Filename:IfcProductsOfCombustionProperties.py
import log
import common
from ifcmaterialproperties import IFCMATERIALPROPERTIES

from utils import *

class IFCPRODUCTSOFCOMBUSTIONPROPERTIES(IFCMATERIALPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCPRODUCTSOFCOMBUSTIONPROPERTIES,self).__init__(id,arg)
        self.type='IFCPRODUCTSOFCOMBUSTIONPROPERTIES'
        self.inverse={}
        self.SpecificHeatCapacity=None #IfcSpecificHeatCapacityMeasure
        self.N20Content=None #IfcPositiveRatioMeasure
        self.COContent=None #IfcPositiveRatioMeasure
        self.CO2Content=None #IfcPositiveRatioMeasure


    def load(self):
        """register inverses"""
        if not super(IFCPRODUCTSOFCOMBUSTIONPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPRODUCTSOFCOMBUSTIONPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SpecificHeatCapacity= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.N20Content= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.COContent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CO2Content= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPRODUCTSOFCOMBUSTIONPROPERTIES,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCPRODUCTSOFCOMBUSTIONPROPERTIES,self).toString()       
        line += integerToSPF(self.SpecificHeatCapacity)+','
        line += integerToSPF(self.N20Content)+','
        line += integerToSPF(self.COContent)+','
        line += integerToSPF(self.CO2Content)+','

        return line
