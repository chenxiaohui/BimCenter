#!/usr/bin/python
#coding=utf-8
#Filename:IfcMechanicalSteelMaterialProperties.py
import log
import common
from ifcmechanicalmaterialproperties import IFCMECHANICALMATERIALPROPERTIES

from utils import *

class IFCMECHANICALSTEELMATERIALPROPERTIES(IFCMECHANICALMATERIALPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCMECHANICALSTEELMATERIALPROPERTIES,self).__init__(id,arg)
        self.type='IFCMECHANICALSTEELMATERIALPROPERTIES'
        self.inverse={}
        self.YieldStress=None #IfcPressureMeasure
        self.UltimateStress=None #IfcPressureMeasure
        self.UltimateStrain=None #IfcPositiveRatioMeasure
        self.HardeningModule=None #IfcModulusOfElasticityMeasure
        self.ProportionalStress=None #IfcPressureMeasure
        self.PlasticStrain=None #IfcPositiveRatioMeasure
        self.Relaxations=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCMECHANICALSTEELMATERIALPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMECHANICALSTEELMATERIALPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.YieldStress= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UltimateStress= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UltimateStrain= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HardeningModule= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProportionalStress= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PlasticStrain= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Relaxations= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMECHANICALSTEELMATERIALPROPERTIES,self).getAttrCount()+7

    def toString(self):
        """"""
        line=super(IFCMECHANICALSTEELMATERIALPROPERTIES,self).toString()       
        line += integerToSPF(self.YieldStress)+','
        line += integerToSPF(self.UltimateStress)+','
        line += integerToSPF(self.UltimateStrain)+','
        line += integerToSPF(self.HardeningModule)+','
        line += integerToSPF(self.ProportionalStress)+','
        line += integerToSPF(self.PlasticStrain)+','
        line += listParamToSPF(self.Relaxations,idToSPF)+','

        return line
