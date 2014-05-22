#!/usr/bin/python
#coding=utf-8
#Filename:IfcCraneRailFShapeProfileDef.py
import log
import common
from ifcparameterizedprofiledef import IFCPARAMETERIZEDPROFILEDEF

from utils import *

class IFCCRANERAILFSHAPEPROFILEDEF(IFCPARAMETERIZEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCCRANERAILFSHAPEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCCRANERAILFSHAPEPROFILEDEF'
        self.inverse={}
        self.OverallHeight=None #IfcPositiveLengthMeasure
        self.HeadWidth=None #IfcPositiveLengthMeasure
        self.Radius=None #IfcPositiveLengthMeasure
        self.HeadDepth2=None #IfcPositiveLengthMeasure
        self.HeadDepth3=None #IfcPositiveLengthMeasure
        self.WebThickness=None #IfcPositiveLengthMeasure
        self.BaseDepth1=None #IfcPositiveLengthMeasure
        self.BaseDepth2=None #IfcPositiveLengthMeasure
        self.CentreOfGravityInY=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCRANERAILFSHAPEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCRANERAILFSHAPEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OverallHeight= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HeadWidth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Radius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HeadDepth2= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HeadDepth3= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WebThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BaseDepth1= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BaseDepth2= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CentreOfGravityInY= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCRANERAILFSHAPEPROFILEDEF,self).getAttrCount()+9

    def toString(self):
        """"""
        line=super(IFCCRANERAILFSHAPEPROFILEDEF,self).toString()       
        line += integerToSPF(self.OverallHeight)+','
        line += integerToSPF(self.HeadWidth)+','
        line += integerToSPF(self.Radius)+','
        line += integerToSPF(self.HeadDepth2)+','
        line += integerToSPF(self.HeadDepth3)+','
        line += integerToSPF(self.WebThickness)+','
        line += integerToSPF(self.BaseDepth1)+','
        line += integerToSPF(self.BaseDepth2)+','
        line += integerToSPF(self.CentreOfGravityInY)+','

        return line
