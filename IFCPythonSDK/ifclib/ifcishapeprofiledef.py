#!/usr/bin/python
#coding=utf-8
#Filename:IfcIShapeProfileDef.py
import log
import common
from ifcparameterizedprofiledef import IFCPARAMETERIZEDPROFILEDEF

from utils import *

class IFCISHAPEPROFILEDEF(IFCPARAMETERIZEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCISHAPEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCISHAPEPROFILEDEF'
        self.inverse={}
        self.OverallWidth=None #IfcPositiveLengthMeasure
        self.OverallDepth=None #IfcPositiveLengthMeasure
        self.WebThickness=None #IfcPositiveLengthMeasure
        self.FlangeThickness=None #IfcPositiveLengthMeasure
        self.FilletRadius=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCISHAPEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCISHAPEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OverallWidth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OverallDepth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WebThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FlangeThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FilletRadius= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCISHAPEPROFILEDEF,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCISHAPEPROFILEDEF,self).toString()       
        line += integerToSPF(self.OverallWidth)+','
        line += integerToSPF(self.OverallDepth)+','
        line += integerToSPF(self.WebThickness)+','
        line += integerToSPF(self.FlangeThickness)+','
        line += integerToSPF(self.FilletRadius)+','

        return line
