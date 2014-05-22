#!/usr/bin/python
#coding=utf-8
#Filename:IfcLightSourcePositional.py
import log
import common
from ifclightsource import IFCLIGHTSOURCE

from utils import *

class IFCLIGHTSOURCEPOSITIONAL(IFCLIGHTSOURCE):
    """"""
    def __init__(self,id,arg):
        super(IFCLIGHTSOURCEPOSITIONAL,self).__init__(id,arg)
        self.type='IFCLIGHTSOURCEPOSITIONAL'
        self.inverse={}
        self.Position=None #IfcCartesianPoint
        self.Radius=None #IfcPositiveLengthMeasure
        self.ConstantAttenuation=None #IfcReal
        self.DistanceAttenuation=None #IfcReal
        self.QuadricAttenuation=None #IfcReal


    def load(self):
        """register inverses"""
        if not super(IFCLIGHTSOURCEPOSITIONAL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLIGHTSOURCEPOSITIONAL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Position= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Radius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConstantAttenuation= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DistanceAttenuation= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.QuadricAttenuation= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLIGHTSOURCEPOSITIONAL,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCLIGHTSOURCEPOSITIONAL,self).toString()       
        line += idToSPF(self.Position)+','
        line += integerToSPF(self.Radius)+','
        line += integerToSPF(self.ConstantAttenuation)+','
        line += integerToSPF(self.DistanceAttenuation)+','
        line += integerToSPF(self.QuadricAttenuation)+','

        return line
