#!/usr/bin/python
#coding=utf-8
#Filename:IfcZShapeProfileDef.py
import log
import common
from ifcparameterizedprofiledef import IFCPARAMETERIZEDPROFILEDEF

from utils import *

class IFCZSHAPEPROFILEDEF(IFCPARAMETERIZEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCZSHAPEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCZSHAPEPROFILEDEF'
        self.inverse={}
        self.Depth=None #IfcPositiveLengthMeasure
        self.FlangeWidth=None #IfcPositiveLengthMeasure
        self.WebThickness=None #IfcPositiveLengthMeasure
        self.FlangeThickness=None #IfcPositiveLengthMeasure
        self.FilletRadius=None #IfcPositiveLengthMeasure
        self.EdgeRadius=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCZSHAPEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCZSHAPEPROFILEDEF,self).init():
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

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCZSHAPEPROFILEDEF,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCZSHAPEPROFILEDEF,self).toString()       
        line += integerToSPF(self.Depth)+','
        line += integerToSPF(self.FlangeWidth)+','
        line += integerToSPF(self.WebThickness)+','
        line += integerToSPF(self.FlangeThickness)+','
        line += integerToSPF(self.FilletRadius)+','
        line += integerToSPF(self.EdgeRadius)+','

        return line
