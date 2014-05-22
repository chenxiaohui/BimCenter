#!/usr/bin/python
#coding=utf-8
#Filename:IfcSoundValue.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCSOUNDVALUE(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCSOUNDVALUE,self).__init__(id,arg)
        self.type='IFCSOUNDVALUE'
        self.inverse={}
        self.SoundLevelTimeSeries=None #IfcTimeSeries
        self.Frequency=None #IfcFrequencyMeasure
        self.SoundLevelSingleValue=None #IfcDerivedMeasureValue


    def load(self):
        """register inverses"""
        if not super(IFCSOUNDVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSOUNDVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SoundLevelTimeSeries= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Frequency= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SoundLevelSingleValue= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSOUNDVALUE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCSOUNDVALUE,self).toString()       
        line += idToSPF(self.SoundLevelTimeSeries)+','
        line += integerToSPF(self.Frequency)+','
        line += typerefToSPF(self.SoundLevelSingleValue)+','

        return line
