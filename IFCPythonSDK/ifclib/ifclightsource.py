#!/usr/bin/python
#coding=utf-8
#Filename:IfcLightSource.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCLIGHTSOURCE(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCLIGHTSOURCE,self).__init__(id,arg)
        self.type='IFCLIGHTSOURCE'
        self.inverse={}
        self.Name=None #IfcLabel
        self.LightColour=None #IfcColourRgb
        self.AmbientIntensity=None #IfcNormalisedRatioMeasure
        self.Intensity=None #IfcNormalisedRatioMeasure


    def load(self):
        """register inverses"""
        if not super(IFCLIGHTSOURCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLIGHTSOURCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LightColour= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AmbientIntensity= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Intensity= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLIGHTSOURCE,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCLIGHTSOURCE,self).toString()       
        line += strToSPF(self.Name)+','
        line += idToSPF(self.LightColour)+','
        line += integerToSPF(self.AmbientIntensity)+','
        line += integerToSPF(self.Intensity)+','

        return line
