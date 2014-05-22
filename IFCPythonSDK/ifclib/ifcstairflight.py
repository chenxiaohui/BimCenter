#!/usr/bin/python
#coding=utf-8
#Filename:IfcStairFlight.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCSTAIRFLIGHT(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCSTAIRFLIGHT,self).__init__(id,arg)
        self.type='IFCSTAIRFLIGHT'
        self.inverse={}
        self.NumberOfRiser=None #INTEGER
        self.NumberOfTreads=None #INTEGER
        self.RiserHeight=None #IfcPositiveLengthMeasure
        self.TreadLength=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSTAIRFLIGHT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTAIRFLIGHT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.NumberOfRiser= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.NumberOfTreads= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RiserHeight= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TreadLength= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTAIRFLIGHT,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCSTAIRFLIGHT,self).toString()       
        line += integerToSPF(self.NumberOfRiser)+','
        line += integerToSPF(self.NumberOfTreads)+','
        line += integerToSPF(self.RiserHeight)+','
        line += integerToSPF(self.TreadLength)+','

        return line
