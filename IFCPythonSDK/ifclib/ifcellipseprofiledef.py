#!/usr/bin/python
#coding=utf-8
#Filename:IfcEllipseProfileDef.py
import log
import common
from ifcparameterizedprofiledef import IFCPARAMETERIZEDPROFILEDEF

from utils import *

class IFCELLIPSEPROFILEDEF(IFCPARAMETERIZEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCELLIPSEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCELLIPSEPROFILEDEF'
        self.inverse={}
        self.SemiAxis1=None #IfcPositiveLengthMeasure
        self.SemiAxis2=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCELLIPSEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELLIPSEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SemiAxis1= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SemiAxis2= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELLIPSEPROFILEDEF,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCELLIPSEPROFILEDEF,self).toString()       
        line += integerToSPF(self.SemiAxis1)+','
        line += integerToSPF(self.SemiAxis2)+','

        return line
