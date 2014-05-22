#!/usr/bin/python
#coding=utf-8
#Filename:IfcConnectionPointEccentricity.py
import log
import common
from ifcconnectionpointgeometry import IFCCONNECTIONPOINTGEOMETRY

from utils import *

class IFCCONNECTIONPOINTECCENTRICITY(IFCCONNECTIONPOINTGEOMETRY):
    """"""
    def __init__(self,id,arg):
        super(IFCCONNECTIONPOINTECCENTRICITY,self).__init__(id,arg)
        self.type='IFCCONNECTIONPOINTECCENTRICITY'
        self.inverse={}
        self.EccentricityInX=None #IfcLengthMeasure
        self.EccentricityInY=None #IfcLengthMeasure
        self.EccentricityInZ=None #IfcLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCONNECTIONPOINTECCENTRICITY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONNECTIONPOINTECCENTRICITY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EccentricityInX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EccentricityInY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EccentricityInZ= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONNECTIONPOINTECCENTRICITY,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCCONNECTIONPOINTECCENTRICITY,self).toString()       
        line += integerToSPF(self.EccentricityInX)+','
        line += integerToSPF(self.EccentricityInY)+','
        line += integerToSPF(self.EccentricityInZ)+','

        return line
