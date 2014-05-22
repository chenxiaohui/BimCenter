#!/usr/bin/python
#coding=utf-8
#Filename:IfcMechanicalConcreteMaterialProperties.py
import log
import common
from ifcmechanicalmaterialproperties import IFCMECHANICALMATERIALPROPERTIES

from utils import *

class IFCMECHANICALCONCRETEMATERIALPROPERTIES(IFCMECHANICALMATERIALPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCMECHANICALCONCRETEMATERIALPROPERTIES,self).__init__(id,arg)
        self.type='IFCMECHANICALCONCRETEMATERIALPROPERTIES'
        self.inverse={}
        self.CompressiveStrength=None #IfcPressureMeasure
        self.MaxAggregateSize=None #IfcPositiveLengthMeasure
        self.AdmixturesDescription=None #IfcText
        self.Workability=None #IfcText
        self.ProtectivePoreRatio=None #IfcNormalisedRatioMeasure
        self.WaterImpermeability=None #IfcText


    def load(self):
        """register inverses"""
        if not super(IFCMECHANICALCONCRETEMATERIALPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMECHANICALCONCRETEMATERIALPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CompressiveStrength= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MaxAggregateSize= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AdmixturesDescription= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Workability= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProtectivePoreRatio= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WaterImpermeability= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMECHANICALCONCRETEMATERIALPROPERTIES,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCMECHANICALCONCRETEMATERIALPROPERTIES,self).toString()       
        line += integerToSPF(self.CompressiveStrength)+','
        line += integerToSPF(self.MaxAggregateSize)+','
        line += strToSPF(self.AdmixturesDescription)+','
        line += strToSPF(self.Workability)+','
        line += integerToSPF(self.ProtectivePoreRatio)+','
        line += strToSPF(self.WaterImpermeability)+','

        return line
