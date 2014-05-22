#!/usr/bin/python
#coding=utf-8
#Filename:IfcElectricalBaseProperties.py
import log
import common
from ifcenergyproperties import IFCENERGYPROPERTIES

from utils import *

class IFCELECTRICALBASEPROPERTIES(IFCENERGYPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCELECTRICALBASEPROPERTIES,self).__init__(id,arg)
        self.type='IFCELECTRICALBASEPROPERTIES'
        self.inverse={}
        self.ElectricCurrentType=None #IfcElectricCurrentEnum
        self.InputVoltage=None #IfcElectricVoltageMeasure
        self.InputFrequency=None #IfcFrequencyMeasure
        self.FullLoadCurrent=None #IfcElectricCurrentMeasure
        self.MinimumCircuitCurrent=None #IfcElectricCurrentMeasure
        self.MaximumPowerInput=None #IfcPowerMeasure
        self.RatedPowerInput=None #IfcPowerMeasure
        self.InputPhase=None #INTEGER


    def load(self):
        """register inverses"""
        if not super(IFCELECTRICALBASEPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELECTRICALBASEPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ElectricCurrentType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InputVoltage= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InputFrequency= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FullLoadCurrent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MinimumCircuitCurrent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MaximumPowerInput= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RatedPowerInput= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InputPhase= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELECTRICALBASEPROPERTIES,self).getAttrCount()+8

    def toString(self):
        """"""
        line=super(IFCELECTRICALBASEPROPERTIES,self).toString()       
        line += typerefToSPF(self.ElectricCurrentType)+','
        line += integerToSPF(self.InputVoltage)+','
        line += integerToSPF(self.InputFrequency)+','
        line += integerToSPF(self.FullLoadCurrent)+','
        line += integerToSPF(self.MinimumCircuitCurrent)+','
        line += integerToSPF(self.MaximumPowerInput)+','
        line += integerToSPF(self.RatedPowerInput)+','
        line += integerToSPF(self.InputPhase)+','

        return line
