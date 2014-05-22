#!/usr/bin/python
#coding=utf-8
#Filename:IfcLShapeProfileDef.py
import log
import common
from ifcparameterizedprofiledef import IFCPARAMETERIZEDPROFILEDEF

from utils import *

class IFCLSHAPEPROFILEDEF(IFCPARAMETERIZEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCLSHAPEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCLSHAPEPROFILEDEF'
        self.inverse={}
        self.Depth=None #IfcPositiveLengthMeasure
        self.Width=None #IfcPositiveLengthMeasure
        self.Thickness=None #IfcPositiveLengthMeasure
        self.FilletRadius=None #IfcPositiveLengthMeasure
        self.EdgeRadius=None #IfcPositiveLengthMeasure
        self.LegSlope=None #IfcPlaneAngleMeasure
        self.CentreOfGravityInX=None #IfcPositiveLengthMeasure
        self.CentreOfGravityInY=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCLSHAPEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLSHAPEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Depth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Width= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Thickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FilletRadius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EdgeRadius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LegSlope= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CentreOfGravityInX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CentreOfGravityInY= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLSHAPEPROFILEDEF,self).getAttrCount()+8

    def toString(self):
        """"""
        line=super(IFCLSHAPEPROFILEDEF,self).toString()       
        line += integerToSPF(self.Depth)+','
        line += integerToSPF(self.Width)+','
        line += integerToSPF(self.Thickness)+','
        line += integerToSPF(self.FilletRadius)+','
        line += integerToSPF(self.EdgeRadius)+','
        line += integerToSPF(self.LegSlope)+','
        line += integerToSPF(self.CentreOfGravityInX)+','
        line += integerToSPF(self.CentreOfGravityInY)+','

        return line
