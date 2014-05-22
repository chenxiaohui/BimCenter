#!/usr/bin/python
#coding=utf-8
#Filename:IfcMechanicalFastener.py
import log
import common
from ifcfastener import IFCFASTENER

from utils import *

class IFCMECHANICALFASTENER(IFCFASTENER):
    """"""
    def __init__(self,id,arg):
        super(IFCMECHANICALFASTENER,self).__init__(id,arg)
        self.type='IFCMECHANICALFASTENER'
        self.inverse={}
        self.NominalDiameter=None #IfcPositiveLengthMeasure
        self.NominalLength=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCMECHANICALFASTENER,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMECHANICALFASTENER,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.NominalDiameter= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.NominalLength= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMECHANICALFASTENER,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCMECHANICALFASTENER,self).toString()       
        line += integerToSPF(self.NominalDiameter)+','
        line += integerToSPF(self.NominalLength)+','

        return line
