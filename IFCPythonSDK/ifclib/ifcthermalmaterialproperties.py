#!/usr/bin/python
#coding=utf-8
#Filename:IfcThermalMaterialProperties.py
import log
import common
from ifcmaterialproperties import IFCMATERIALPROPERTIES

from utils import *

class IFCTHERMALMATERIALPROPERTIES(IFCMATERIALPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCTHERMALMATERIALPROPERTIES,self).__init__(id,arg)
        self.type='IFCTHERMALMATERIALPROPERTIES'
        self.inverse={}
        self.SpecificHeatCapacity=None #IfcSpecificHeatCapacityMeasure
        self.BoilingPoint=None #IfcThermodynamicTemperatureMeasure
        self.FreezingPoint=None #IfcThermodynamicTemperatureMeasure
        self.ThermalConductivity=None #IfcThermalConductivityMeasure


    def load(self):
        """register inverses"""
        if not super(IFCTHERMALMATERIALPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTHERMALMATERIALPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SpecificHeatCapacity= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BoilingPoint= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FreezingPoint= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThermalConductivity= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTHERMALMATERIALPROPERTIES,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCTHERMALMATERIALPROPERTIES,self).toString()       
        line += integerToSPF(self.SpecificHeatCapacity)+','
        line += integerToSPF(self.BoilingPoint)+','
        line += integerToSPF(self.FreezingPoint)+','
        line += integerToSPF(self.ThermalConductivity)+','

        return line
