#!/usr/bin/python
#coding=utf-8
#Filename:IfcTrapeziumProfileDef.py
import log
import common
from ifcparameterizedprofiledef import IFCPARAMETERIZEDPROFILEDEF

from utils import *

class IFCTRAPEZIUMPROFILEDEF(IFCPARAMETERIZEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCTRAPEZIUMPROFILEDEF,self).__init__(id,arg)
        self.type='IFCTRAPEZIUMPROFILEDEF'
        self.inverse={}
        self.BottomXDim=None #IfcPositiveLengthMeasure
        self.TopXDim=None #IfcPositiveLengthMeasure
        self.YDim=None #IfcPositiveLengthMeasure
        self.TopXOffset=None #IfcLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCTRAPEZIUMPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTRAPEZIUMPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BottomXDim= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TopXDim= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.YDim= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TopXOffset= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTRAPEZIUMPROFILEDEF,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCTRAPEZIUMPROFILEDEF,self).toString()       
        line += integerToSPF(self.BottomXDim)+','
        line += integerToSPF(self.TopXDim)+','
        line += integerToSPF(self.YDim)+','
        line += integerToSPF(self.TopXOffset)+','

        return line
