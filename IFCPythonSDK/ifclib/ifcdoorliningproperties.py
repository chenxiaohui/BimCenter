#!/usr/bin/python
#coding=utf-8
#Filename:IfcDoorLiningProperties.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCDOORLININGPROPERTIES(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCDOORLININGPROPERTIES,self).__init__(id,arg)
        self.type='IFCDOORLININGPROPERTIES'
        self.inverse={}
        self.LiningDepth=None #IfcPositiveLengthMeasure
        self.LiningThickness=None #IfcPositiveLengthMeasure
        self.ThresholdDepth=None #IfcPositiveLengthMeasure
        self.ThresholdThickness=None #IfcPositiveLengthMeasure
        self.TransomThickness=None #IfcPositiveLengthMeasure
        self.TransomOffset=None #IfcLengthMeasure
        self.LiningOffset=None #IfcLengthMeasure
        self.ThresholdOffset=None #IfcLengthMeasure
        self.CasingThickness=None #IfcPositiveLengthMeasure
        self.CasingDepth=None #IfcPositiveLengthMeasure
        self.ShapeAspectStyle=None #IfcShapeAspect


    def load(self):
        """register inverses"""
        if not super(IFCDOORLININGPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDOORLININGPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LiningDepth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LiningThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThresholdDepth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThresholdThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TransomThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TransomOffset= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LiningOffset= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThresholdOffset= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CasingThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CasingDepth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShapeAspectStyle= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDOORLININGPROPERTIES,self).getAttrCount()+11

    def toString(self):
        """"""
        line=super(IFCDOORLININGPROPERTIES,self).toString()       
        line += integerToSPF(self.LiningDepth)+','
        line += integerToSPF(self.LiningThickness)+','
        line += integerToSPF(self.ThresholdDepth)+','
        line += integerToSPF(self.ThresholdThickness)+','
        line += integerToSPF(self.TransomThickness)+','
        line += integerToSPF(self.TransomOffset)+','
        line += integerToSPF(self.LiningOffset)+','
        line += integerToSPF(self.ThresholdOffset)+','
        line += integerToSPF(self.CasingThickness)+','
        line += integerToSPF(self.CasingDepth)+','
        line += idToSPF(self.ShapeAspectStyle)+','

        return line
