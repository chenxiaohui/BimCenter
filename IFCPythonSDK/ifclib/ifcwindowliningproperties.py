#!/usr/bin/python
#coding=utf-8
#Filename:IfcWindowLiningProperties.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCWINDOWLININGPROPERTIES(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCWINDOWLININGPROPERTIES,self).__init__(id,arg)
        self.type='IFCWINDOWLININGPROPERTIES'
        self.inverse={}
        self.LiningDepth=None #IfcPositiveLengthMeasure
        self.LiningThickness=None #IfcPositiveLengthMeasure
        self.TransomThickness=None #IfcPositiveLengthMeasure
        self.MullionThickness=None #IfcPositiveLengthMeasure
        self.FirstTransomOffset=None #IfcNormalisedRatioMeasure
        self.SecondTransomOffset=None #IfcNormalisedRatioMeasure
        self.FirstMullionOffset=None #IfcNormalisedRatioMeasure
        self.SecondMullionOffset=None #IfcNormalisedRatioMeasure
        self.ShapeAspectStyle=None #IfcShapeAspect


    def load(self):
        """register inverses"""
        if not super(IFCWINDOWLININGPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWINDOWLININGPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LiningDepth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LiningThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TransomThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MullionThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FirstTransomOffset= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SecondTransomOffset= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FirstMullionOffset= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SecondMullionOffset= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShapeAspectStyle= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCWINDOWLININGPROPERTIES,self).getAttrCount()+9

    def toString(self):
        """"""
        line=super(IFCWINDOWLININGPROPERTIES,self).toString()       
        line += integerToSPF(self.LiningDepth)+','
        line += integerToSPF(self.LiningThickness)+','
        line += integerToSPF(self.TransomThickness)+','
        line += integerToSPF(self.MullionThickness)+','
        line += integerToSPF(self.FirstTransomOffset)+','
        line += integerToSPF(self.SecondTransomOffset)+','
        line += integerToSPF(self.FirstMullionOffset)+','
        line += integerToSPF(self.SecondMullionOffset)+','
        line += idToSPF(self.ShapeAspectStyle)+','

        return line
