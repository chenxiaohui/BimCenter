#!/usr/bin/python
#coding=utf-8
#Filename:IfcFuelProperties.py
import log
import common
from ifcmaterialproperties import IFCMATERIALPROPERTIES

from utils import *

class IFCFUELPROPERTIES(IFCMATERIALPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCFUELPROPERTIES,self).__init__(id,arg)
        self.type='IFCFUELPROPERTIES'
        self.inverse={}
        self.CombustionTemperature=None #IfcThermodynamicTemperatureMeasure
        self.CarbonContent=None #IfcPositiveRatioMeasure
        self.LowerHeatingValue=None #IfcHeatingValueMeasure
        self.HigherHeatingValue=None #IfcHeatingValueMeasure


    def load(self):
        """register inverses"""
        if not super(IFCFUELPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFUELPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CombustionTemperature= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CarbonContent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LowerHeatingValue= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HigherHeatingValue= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFUELPROPERTIES,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCFUELPROPERTIES,self).toString()       
        line += integerToSPF(self.CombustionTemperature)+','
        line += integerToSPF(self.CarbonContent)+','
        line += integerToSPF(self.LowerHeatingValue)+','
        line += integerToSPF(self.HigherHeatingValue)+','

        return line
