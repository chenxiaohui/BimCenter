#!/usr/bin/python
#coding=utf-8
#Filename:IfcOpticalMaterialProperties.py
import log
import common
from ifcmaterialproperties import IFCMATERIALPROPERTIES

from utils import *

class IFCOPTICALMATERIALPROPERTIES(IFCMATERIALPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCOPTICALMATERIALPROPERTIES,self).__init__(id,arg)
        self.type='IFCOPTICALMATERIALPROPERTIES'
        self.inverse={}
        self.VisibleTransmittance=None #IfcPositiveRatioMeasure
        self.SolarTransmittance=None #IfcPositiveRatioMeasure
        self.ThermalIrTransmittance=None #IfcPositiveRatioMeasure
        self.ThermalIrEmissivityBack=None #IfcPositiveRatioMeasure
        self.ThermalIrEmissivityFront=None #IfcPositiveRatioMeasure
        self.VisibleReflectanceBack=None #IfcPositiveRatioMeasure
        self.VisibleReflectanceFront=None #IfcPositiveRatioMeasure
        self.SolarReflectanceFront=None #IfcPositiveRatioMeasure
        self.SolarReflectanceBack=None #IfcPositiveRatioMeasure


    def load(self):
        """register inverses"""
        if not super(IFCOPTICALMATERIALPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCOPTICALMATERIALPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VisibleTransmittance= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SolarTransmittance= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThermalIrTransmittance= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThermalIrEmissivityBack= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThermalIrEmissivityFront= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VisibleReflectanceBack= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VisibleReflectanceFront= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SolarReflectanceFront= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SolarReflectanceBack= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCOPTICALMATERIALPROPERTIES,self).getAttrCount()+9

    def toString(self):
        """"""
        line=super(IFCOPTICALMATERIALPROPERTIES,self).toString()       
        line += integerToSPF(self.VisibleTransmittance)+','
        line += integerToSPF(self.SolarTransmittance)+','
        line += integerToSPF(self.ThermalIrTransmittance)+','
        line += integerToSPF(self.ThermalIrEmissivityBack)+','
        line += integerToSPF(self.ThermalIrEmissivityFront)+','
        line += integerToSPF(self.VisibleReflectanceBack)+','
        line += integerToSPF(self.VisibleReflectanceFront)+','
        line += integerToSPF(self.SolarReflectanceFront)+','
        line += integerToSPF(self.SolarReflectanceBack)+','

        return line
