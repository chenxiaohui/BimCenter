#!/usr/bin/python
#coding=utf-8
#Filename:IfcFillAreaStyleHatching.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCFILLAREASTYLEHATCHING(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCFILLAREASTYLEHATCHING,self).__init__(id,arg)
        self.type='IFCFILLAREASTYLEHATCHING'
        self.inverse={}
        self.HatchLineAppearance=None #IfcCurveStyle
        self.StartOfNextHatchLine=None #IfcHatchLineDistanceSelect
        self.PointOfReferenceHatchLine=None #IfcCartesianPoint
        self.PatternStart=None #IfcCartesianPoint
        self.HatchLineAngle=None #IfcPlaneAngleMeasure


    def load(self):
        """register inverses"""
        if not super(IFCFILLAREASTYLEHATCHING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFILLAREASTYLEHATCHING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HatchLineAppearance= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.StartOfNextHatchLine= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PointOfReferenceHatchLine= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PatternStart= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HatchLineAngle= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFILLAREASTYLEHATCHING,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCFILLAREASTYLEHATCHING,self).toString()       
        line += idToSPF(self.HatchLineAppearance)+','
        line += typerefToSPF(self.StartOfNextHatchLine)+','
        line += idToSPF(self.PointOfReferenceHatchLine)+','
        line += idToSPF(self.PatternStart)+','
        line += integerToSPF(self.HatchLineAngle)+','

        return line
