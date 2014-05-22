#!/usr/bin/python
#coding=utf-8
#Filename:IfcCircleProfileDef.py
import log
import common
from ifcparameterizedprofiledef import IFCPARAMETERIZEDPROFILEDEF

from utils import *

class IFCCIRCLEPROFILEDEF(IFCPARAMETERIZEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCCIRCLEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCCIRCLEPROFILEDEF'
        self.inverse={}
        self.Radius=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCIRCLEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCIRCLEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Radius= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCIRCLEPROFILEDEF,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCIRCLEPROFILEDEF,self).toString()       
        line += integerToSPF(self.Radius)+','

        return line
