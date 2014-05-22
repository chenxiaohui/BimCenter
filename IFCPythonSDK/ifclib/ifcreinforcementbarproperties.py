#!/usr/bin/python
#coding=utf-8
#Filename:IfcReinforcementBarProperties.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCREINFORCEMENTBARPROPERTIES(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCREINFORCEMENTBARPROPERTIES,self).__init__(id,arg)
        self.type='IFCREINFORCEMENTBARPROPERTIES'
        self.inverse={}
        self.TotalCrossSectionArea=None #IfcAreaMeasure
        self.SteelGrade=None #IfcLabel
        self.BarSurface=None #IfcReinforcingBarSurfaceEnum
        self.EffectiveDepth=None #IfcLengthMeasure
        self.NominalBarDiameter=None #IfcPositiveLengthMeasure
        self.BarCount=None #IfcCountMeasure


    def load(self):
        """register inverses"""
        if not super(IFCREINFORCEMENTBARPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREINFORCEMENTBARPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TotalCrossSectionArea= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SteelGrade= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BarSurface= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EffectiveDepth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.NominalBarDiameter= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BarCount= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREINFORCEMENTBARPROPERTIES,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCREINFORCEMENTBARPROPERTIES,self).toString()       
        line += integerToSPF(self.TotalCrossSectionArea)+','
        line += strToSPF(self.SteelGrade)+','
        line += typerefToSPF(self.BarSurface)+','
        line += integerToSPF(self.EffectiveDepth)+','
        line += integerToSPF(self.NominalBarDiameter)+','
        line += integerToSPF(self.BarCount)+','

        return line
