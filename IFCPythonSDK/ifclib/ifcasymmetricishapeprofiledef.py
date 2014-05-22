#!/usr/bin/python
#coding=utf-8
#Filename:IfcAsymmetricIShapeProfileDef.py
import log
import common
from ifcishapeprofiledef import IFCISHAPEPROFILEDEF

from utils import *

class IFCASYMMETRICISHAPEPROFILEDEF(IFCISHAPEPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCASYMMETRICISHAPEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCASYMMETRICISHAPEPROFILEDEF'
        self.inverse={}
        self.TopFlangeWidth=None #IfcPositiveLengthMeasure
        self.TopFlangeThickness=None #IfcPositiveLengthMeasure
        self.TopFlangeFilletRadius=None #IfcPositiveLengthMeasure
        self.CentreOfGravityInY=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCASYMMETRICISHAPEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCASYMMETRICISHAPEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TopFlangeWidth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TopFlangeThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TopFlangeFilletRadius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CentreOfGravityInY= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCASYMMETRICISHAPEPROFILEDEF,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCASYMMETRICISHAPEPROFILEDEF,self).toString()       
        line += integerToSPF(self.TopFlangeWidth)+','
        line += integerToSPF(self.TopFlangeThickness)+','
        line += integerToSPF(self.TopFlangeFilletRadius)+','
        line += integerToSPF(self.CentreOfGravityInY)+','

        return line
