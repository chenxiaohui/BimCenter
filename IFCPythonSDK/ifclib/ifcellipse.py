#!/usr/bin/python
#coding=utf-8
#Filename:IfcEllipse.py
import log
import common
from ifcconic import IFCCONIC

from utils import *

class IFCELLIPSE(IFCCONIC):
    """"""
    def __init__(self,id,arg):
        super(IFCELLIPSE,self).__init__(id,arg)
        self.type='IFCELLIPSE'
        self.inverse={}
        self.SemiAxis1=None #IfcPositiveLengthMeasure
        self.SemiAxis2=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCELLIPSE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELLIPSE,self).init():
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
        return super(IFCELLIPSE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCELLIPSE,self).toString()       
        line += integerToSPF(self.SemiAxis1)+','
        line += integerToSPF(self.SemiAxis2)+','

        return line
