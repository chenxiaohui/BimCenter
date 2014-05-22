#!/usr/bin/python
#coding=utf-8
#Filename:IfcLightSourceGoniometric.py
import log
import common
from ifclightsource import IFCLIGHTSOURCE

from utils import *

class IFCLIGHTSOURCEGONIOMETRIC(IFCLIGHTSOURCE):
    """"""
    def __init__(self,id,arg):
        super(IFCLIGHTSOURCEGONIOMETRIC,self).__init__(id,arg)
        self.type='IFCLIGHTSOURCEGONIOMETRIC'
        self.inverse={}
        self.Position=None #IfcAxis2Placement3D
        self.ColourAppearance=None #IfcColourRgb
        self.ColourTemperature=None #IfcThermodynamicTemperatureMeasure
        self.LuminousFlux=None #IfcLuminousFluxMeasure
        self.LightEmissionSource=None #IfcLightEmissionSourceEnum
        self.LightDistributionDataSource=None #IfcLightDistributionDataSourceSelect


    def load(self):
        """register inverses"""
        if not super(IFCLIGHTSOURCEGONIOMETRIC,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLIGHTSOURCEGONIOMETRIC,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Position= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ColourAppearance= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ColourTemperature= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LuminousFlux= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LightEmissionSource= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LightDistributionDataSource= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLIGHTSOURCEGONIOMETRIC,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCLIGHTSOURCEGONIOMETRIC,self).toString()       
        line += idToSPF(self.Position)+','
        line += idToSPF(self.ColourAppearance)+','
        line += integerToSPF(self.ColourTemperature)+','
        line += integerToSPF(self.LuminousFlux)+','
        line += typerefToSPF(self.LightEmissionSource)+','
        line += typerefToSPF(self.LightDistributionDataSource)+','

        return line
