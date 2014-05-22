#!/usr/bin/python
#coding=utf-8
#Filename:IfcTShapeProfileDef.py
import log
import common
from ifcparameterizedprofiledef import IFCPARAMETERIZEDPROFILEDEF

from utils import *

class IFCTSHAPEPROFILEDEF(IFCPARAMETERIZEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCTSHAPEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCTSHAPEPROFILEDEF'
        self.inverse={}
        self.Depth=None #IfcPositiveLengthMeasure
        self.FlangeWidth=None #IfcPositiveLengthMeasure
        self.WebThickness=None #IfcPositiveLengthMeasure
        self.FlangeThickness=None #IfcPositiveLengthMeasure
        self.FilletRadius=None #IfcPositiveLengthMeasure
        self.FlangeEdgeRadius=None #IfcPositiveLengthMeasure
        self.WebEdgeRadius=None #IfcPositiveLengthMeasure
        self.WebSlope=None #IfcPlaneAngleMeasure
        self.FlangeSlope=None #IfcPlaneAngleMeasure
        self.CentreOfGravityInY=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCTSHAPEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTSHAPEPROFILEDEF,self).init():
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
            self.FlangeEdgeRadius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WebEdgeRadius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WebSlope= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FlangeSlope= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CentreOfGravityInY= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTSHAPEPROFILEDEF,self).getAttrCount()+10

    def toString(self):
        """"""
        line=super(IFCTSHAPEPROFILEDEF,self).toString()       
        line += integerToSPF(self.Depth)+','
        line += integerToSPF(self.FlangeWidth)+','
        line += integerToSPF(self.WebThickness)+','
        line += integerToSPF(self.FlangeThickness)+','
        line += integerToSPF(self.FilletRadius)+','
        line += integerToSPF(self.FlangeEdgeRadius)+','
        line += integerToSPF(self.WebEdgeRadius)+','
        line += integerToSPF(self.WebSlope)+','
        line += integerToSPF(self.FlangeSlope)+','
        line += integerToSPF(self.CentreOfGravityInY)+','

        return line
