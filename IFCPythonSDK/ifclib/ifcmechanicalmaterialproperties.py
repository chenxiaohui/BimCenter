#!/usr/bin/python
#coding=utf-8
#Filename:IfcMechanicalMaterialProperties.py
import log
import common
from ifcmaterialproperties import IFCMATERIALPROPERTIES

from utils import *

class IFCMECHANICALMATERIALPROPERTIES(IFCMATERIALPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCMECHANICALMATERIALPROPERTIES,self).__init__(id,arg)
        self.type='IFCMECHANICALMATERIALPROPERTIES'
        self.inverse={}
        self.DynamicViscosity=None #IfcDynamicViscosityMeasure
        self.YoungModulus=None #IfcModulusOfElasticityMeasure
        self.ShearModulus=None #IfcModulusOfElasticityMeasure
        self.PoissonRatio=None #IfcPositiveRatioMeasure
        self.ThermalExpansionCoefficient=None #IfcThermalExpansionCoefficientMeasure


    def load(self):
        """register inverses"""
        if not super(IFCMECHANICALMATERIALPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMECHANICALMATERIALPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DynamicViscosity= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.YoungModulus= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShearModulus= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PoissonRatio= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThermalExpansionCoefficient= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMECHANICALMATERIALPROPERTIES,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCMECHANICALMATERIALPROPERTIES,self).toString()       
        line += integerToSPF(self.DynamicViscosity)+','
        line += integerToSPF(self.YoungModulus)+','
        line += integerToSPF(self.ShearModulus)+','
        line += integerToSPF(self.PoissonRatio)+','
        line += integerToSPF(self.ThermalExpansionCoefficient)+','

        return line
