#!/usr/bin/python
#coding=utf-8
#Filename:IfcSpaceThermalLoadProperties.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCSPACETHERMALLOADPROPERTIES(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCSPACETHERMALLOADPROPERTIES,self).__init__(id,arg)
        self.type='IFCSPACETHERMALLOADPROPERTIES'
        self.inverse={}
        self.ApplicableValueRatio=None #IfcPositiveRatioMeasure
        self.ThermalLoadSource=None #IfcThermalLoadSourceEnum
        self.PropertySource=None #IfcPropertySourceEnum
        self.SourceDescription=None #IfcText
        self.MaximumValue=None #IfcPowerMeasure
        self.MinimumValue=None #IfcPowerMeasure
        self.ThermalLoadTimeSeriesValues=None #IfcTimeSeries
        self.UserDefinedThermalLoadSource=None #IfcLabel
        self.UserDefinedPropertySource=None #IfcLabel
        self.ThermalLoadType=None #IfcThermalLoadTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSPACETHERMALLOADPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSPACETHERMALLOADPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApplicableValueRatio= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThermalLoadSource= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PropertySource= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SourceDescription= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MaximumValue= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MinimumValue= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThermalLoadTimeSeriesValues= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedThermalLoadSource= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedPropertySource= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThermalLoadType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSPACETHERMALLOADPROPERTIES,self).getAttrCount()+10

    def toString(self):
        """"""
        line=super(IFCSPACETHERMALLOADPROPERTIES,self).toString()       
        line += integerToSPF(self.ApplicableValueRatio)+','
        line += typerefToSPF(self.ThermalLoadSource)+','
        line += typerefToSPF(self.PropertySource)+','
        line += strToSPF(self.SourceDescription)+','
        line += integerToSPF(self.MaximumValue)+','
        line += integerToSPF(self.MinimumValue)+','
        line += idToSPF(self.ThermalLoadTimeSeriesValues)+','
        line += strToSPF(self.UserDefinedThermalLoadSource)+','
        line += strToSPF(self.UserDefinedPropertySource)+','
        line += typerefToSPF(self.ThermalLoadType)+','

        return line
