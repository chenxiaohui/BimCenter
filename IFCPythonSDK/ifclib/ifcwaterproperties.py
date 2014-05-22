#!/usr/bin/python
#coding=utf-8
#Filename:IfcWaterProperties.py
import log
import common
from ifcmaterialproperties import IFCMATERIALPROPERTIES

from utils import *

class IFCWATERPROPERTIES(IFCMATERIALPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCWATERPROPERTIES,self).__init__(id,arg)
        self.type='IFCWATERPROPERTIES'
        self.inverse={}
        self.IsPotable=None #BOOLEAN
        self.Hardness=None #IfcIonConcentrationMeasure
        self.AlkalinityConcentration=None #IfcIonConcentrationMeasure
        self.AcidityConcentration=None #IfcIonConcentrationMeasure
        self.ImpuritiesContent=None #IfcNormalisedRatioMeasure
        self.PHLevel=None #IfcPHMeasure
        self.DissolvedSolidsContent=None #IfcNormalisedRatioMeasure


    def load(self):
        """register inverses"""
        if not super(IFCWATERPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWATERPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.IsPotable= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Hardness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AlkalinityConcentration= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AcidityConcentration= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ImpuritiesContent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PHLevel= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DissolvedSolidsContent= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCWATERPROPERTIES,self).getAttrCount()+7

    def toString(self):
        """"""
        line=super(IFCWATERPROPERTIES,self).toString()       
        line += logicalToSPF(self.IsPotable)+','
        line += integerToSPF(self.Hardness)+','
        line += integerToSPF(self.AlkalinityConcentration)+','
        line += integerToSPF(self.AcidityConcentration)+','
        line += integerToSPF(self.ImpuritiesContent)+','
        line += integerToSPF(self.PHLevel)+','
        line += integerToSPF(self.DissolvedSolidsContent)+','

        return line
