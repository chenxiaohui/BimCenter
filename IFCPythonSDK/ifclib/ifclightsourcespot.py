#!/usr/bin/python
#coding=utf-8
#Filename:IfcLightSourceSpot.py
import log
import common
from ifclightsourcepositional import IFCLIGHTSOURCEPOSITIONAL

from utils import *

class IFCLIGHTSOURCESPOT(IFCLIGHTSOURCEPOSITIONAL):
    """"""
    def __init__(self,id,arg):
        super(IFCLIGHTSOURCESPOT,self).__init__(id,arg)
        self.type='IFCLIGHTSOURCESPOT'
        self.inverse={}
        self.Orientation=None #IfcDirection
        self.ConcentrationExponent=None #IfcReal
        self.SpreadAngle=None #IfcPositivePlaneAngleMeasure
        self.BeamWidthAngle=None #IfcPositivePlaneAngleMeasure


    def load(self):
        """register inverses"""
        if not super(IFCLIGHTSOURCESPOT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLIGHTSOURCESPOT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Orientation= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConcentrationExponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SpreadAngle= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BeamWidthAngle= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLIGHTSOURCESPOT,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCLIGHTSOURCESPOT,self).toString()       
        line += idToSPF(self.Orientation)+','
        line += integerToSPF(self.ConcentrationExponent)+','
        line += integerToSPF(self.SpreadAngle)+','
        line += integerToSPF(self.BeamWidthAngle)+','

        return line
