#!/usr/bin/python
#coding=utf-8
#Filename:IfcFluidFlowProperties.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCFLUIDFLOWPROPERTIES(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCFLUIDFLOWPROPERTIES,self).__init__(id,arg)
        self.type='IFCFLUIDFLOWPROPERTIES'
        self.inverse={}
        self.PropertySource=None #IfcPropertySourceEnum
        self.FlowConditionTimeSeries=None #IfcTimeSeries
        self.VelocityTimeSeries=None #IfcTimeSeries
        self.FlowrateTimeSeries=None #IfcTimeSeries
        self.Fluid=None #IfcMaterial
        self.PressureTimeSeries=None #IfcTimeSeries
        self.UserDefinedPropertySource=None #IfcLabel
        self.TemperatureSingleValue=None #IfcThermodynamicTemperatureMeasure
        self.WetBulbTemperatureSingleValue=None #IfcThermodynamicTemperatureMeasure
        self.WetBulbTemperatureTimeSeries=None #IfcTimeSeries
        self.TemperatureTimeSeries=None #IfcTimeSeries
        self.FlowrateSingleValue=None #IfcDerivedMeasureValue
        self.FlowConditionSingleValue=None #IfcPositiveRatioMeasure
        self.VelocitySingleValue=None #IfcLinearVelocityMeasure
        self.PressureSingleValue=None #IfcPressureMeasure


    def load(self):
        """register inverses"""
        if not super(IFCFLUIDFLOWPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLUIDFLOWPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PropertySource= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FlowConditionTimeSeries= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VelocityTimeSeries= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FlowrateTimeSeries= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Fluid= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PressureTimeSeries= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedPropertySource= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TemperatureSingleValue= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WetBulbTemperatureSingleValue= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WetBulbTemperatureTimeSeries= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TemperatureTimeSeries= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FlowrateSingleValue= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FlowConditionSingleValue= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VelocitySingleValue= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PressureSingleValue= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLUIDFLOWPROPERTIES,self).getAttrCount()+15

    def toString(self):
        """"""
        line=super(IFCFLUIDFLOWPROPERTIES,self).toString()       
        line += typerefToSPF(self.PropertySource)+','
        line += idToSPF(self.FlowConditionTimeSeries)+','
        line += idToSPF(self.VelocityTimeSeries)+','
        line += idToSPF(self.FlowrateTimeSeries)+','
        line += idToSPF(self.Fluid)+','
        line += idToSPF(self.PressureTimeSeries)+','
        line += strToSPF(self.UserDefinedPropertySource)+','
        line += integerToSPF(self.TemperatureSingleValue)+','
        line += integerToSPF(self.WetBulbTemperatureSingleValue)+','
        line += idToSPF(self.WetBulbTemperatureTimeSeries)+','
        line += idToSPF(self.TemperatureTimeSeries)+','
        line += typerefToSPF(self.FlowrateSingleValue)+','
        line += integerToSPF(self.FlowConditionSingleValue)+','
        line += integerToSPF(self.VelocitySingleValue)+','
        line += integerToSPF(self.PressureSingleValue)+','

        return line
