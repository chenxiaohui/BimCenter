#!/usr/bin/python
#coding=utf-8
#Filename:IfcRectangleProfileDef.py
import log
import common
from ifcparameterizedprofiledef import IFCPARAMETERIZEDPROFILEDEF

from utils import *

class IFCRECTANGLEPROFILEDEF(IFCPARAMETERIZEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCRECTANGLEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCRECTANGLEPROFILEDEF'
        self.inverse={}
        self.XDim=None #IfcPositiveLengthMeasure
        self.YDim=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCRECTANGLEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRECTANGLEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.XDim= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.YDim= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRECTANGLEPROFILEDEF,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRECTANGLEPROFILEDEF,self).toString()       
        line += integerToSPF(self.XDim)+','
        line += integerToSPF(self.YDim)+','

        return line
