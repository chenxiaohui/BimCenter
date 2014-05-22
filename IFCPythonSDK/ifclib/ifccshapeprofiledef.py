#!/usr/bin/python
#coding=utf-8
#Filename:IfcCShapeProfileDef.py
import log
import common
from ifcparameterizedprofiledef import IFCPARAMETERIZEDPROFILEDEF

from utils import *

class IFCCSHAPEPROFILEDEF(IFCPARAMETERIZEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCCSHAPEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCCSHAPEPROFILEDEF'
        self.inverse={}
        self.Depth=None #IfcPositiveLengthMeasure
        self.Width=None #IfcPositiveLengthMeasure
        self.WallThickness=None #IfcPositiveLengthMeasure
        self.Girth=None #IfcPositiveLengthMeasure
        self.InternalFilletRadius=None #IfcPositiveLengthMeasure
        self.CentreOfGravityInX=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCSHAPEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCSHAPEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Depth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Width= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WallThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Girth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InternalFilletRadius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CentreOfGravityInX= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCSHAPEPROFILEDEF,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCCSHAPEPROFILEDEF,self).toString()       
        line += integerToSPF(self.Depth)+','
        line += integerToSPF(self.Width)+','
        line += integerToSPF(self.WallThickness)+','
        line += integerToSPF(self.Girth)+','
        line += integerToSPF(self.InternalFilletRadius)+','
        line += integerToSPF(self.CentreOfGravityInX)+','

        return line
