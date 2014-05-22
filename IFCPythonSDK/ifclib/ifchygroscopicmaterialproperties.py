#!/usr/bin/python
#coding=utf-8
#Filename:IfcHygroscopicMaterialProperties.py
import log
import common
from ifcmaterialproperties import IFCMATERIALPROPERTIES

from utils import *

class IFCHYGROSCOPICMATERIALPROPERTIES(IFCMATERIALPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCHYGROSCOPICMATERIALPROPERTIES,self).__init__(id,arg)
        self.type='IFCHYGROSCOPICMATERIALPROPERTIES'
        self.inverse={}
        self.UpperVaporResistanceFactor=None #IfcPositiveRatioMeasure
        self.LowerVaporResistanceFactor=None #IfcPositiveRatioMeasure
        self.IsothermalMoistureCapacity=None #IfcIsothermalMoistureCapacityMeasure
        self.VaporPermeability=None #IfcVaporPermeabilityMeasure
        self.MoistureDiffusivity=None #IfcMoistureDiffusivityMeasure


    def load(self):
        """register inverses"""
        if not super(IFCHYGROSCOPICMATERIALPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCHYGROSCOPICMATERIALPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UpperVaporResistanceFactor= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LowerVaporResistanceFactor= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.IsothermalMoistureCapacity= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VaporPermeability= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MoistureDiffusivity= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCHYGROSCOPICMATERIALPROPERTIES,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCHYGROSCOPICMATERIALPROPERTIES,self).toString()       
        line += integerToSPF(self.UpperVaporResistanceFactor)+','
        line += integerToSPF(self.LowerVaporResistanceFactor)+','
        line += integerToSPF(self.IsothermalMoistureCapacity)+','
        line += integerToSPF(self.VaporPermeability)+','
        line += integerToSPF(self.MoistureDiffusivity)+','

        return line
