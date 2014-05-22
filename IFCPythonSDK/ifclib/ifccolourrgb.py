#!/usr/bin/python
#coding=utf-8
#Filename:IfcColourRgb.py
import log
import common
from ifccolourspecification import IFCCOLOURSPECIFICATION

from utils import *

class IFCCOLOURRGB(IFCCOLOURSPECIFICATION):
    """"""
    def __init__(self,id,arg):
        super(IFCCOLOURRGB,self).__init__(id,arg)
        self.type='IFCCOLOURRGB'
        self.inverse={}
        self.Red=None #IfcNormalisedRatioMeasure
        self.Green=None #IfcNormalisedRatioMeasure
        self.Blue=None #IfcNormalisedRatioMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCOLOURRGB,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOLOURRGB,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Red= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Green= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Blue= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOLOURRGB,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCCOLOURRGB,self).toString()       
        line += integerToSPF(self.Red)+','
        line += integerToSPF(self.Green)+','
        line += integerToSPF(self.Blue)+','

        return line
