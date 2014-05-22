#!/usr/bin/python
#coding=utf-8
#Filename:IfcUShapeProfileDef.py
import log
import common
from ifcparameterizedprofiledef import IFCPARAMETERIZEDPROFILEDEF

from utils import *

class IFCUSHAPEPROFILEDEF(IFCPARAMETERIZEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCUSHAPEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCUSHAPEPROFILEDEF'
        self.inverse={}
        self.Depth=None #IfcPositiveLengthMeasure
        self.FlangeWidth=None #IfcPositiveLengthMeasure
        self.WebThickness=None #IfcPositiveLengthMeasure
        self.FlangeThickness=None #IfcPositiveLengthMeasure
        self.FilletRadius=None #IfcPositiveLengthMeasure
        self.EdgeRadius=None #IfcPositiveLengthMeasure
        self.FlangeSlope=None #IfcPlaneAngleMeasure
        self.CentreOfGravityInX=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCUSHAPEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCUSHAPEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Depth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FlangeWidth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WebThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FlangeThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FilletRadius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EdgeRadius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FlangeSlope= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CentreOfGravityInX= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCUSHAPEPROFILEDEF,self).getAttrCount()+8

    def toString(self):
        """"""
        line=super(IFCUSHAPEPROFILEDEF,self).toString()       
        line += integerToSPF(self.Depth)+','
        line += integerToSPF(self.FlangeWidth)+','
        line += integerToSPF(self.WebThickness)+','
        line += integerToSPF(self.FlangeThickness)+','
        line += integerToSPF(self.FilletRadius)+','
        line += integerToSPF(self.EdgeRadius)+','
        line += integerToSPF(self.FlangeSlope)+','
        line += integerToSPF(self.CentreOfGravityInX)+','

        return line
