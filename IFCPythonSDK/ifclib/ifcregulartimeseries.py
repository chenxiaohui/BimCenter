#!/usr/bin/python
#coding=utf-8
#Filename:IfcRegularTimeSeries.py
import log
import common
from ifctimeseries import IFCTIMESERIES

from utils import *

class IFCREGULARTIMESERIES(IFCTIMESERIES):
    """"""
    def __init__(self,id,arg):
        super(IFCREGULARTIMESERIES,self).__init__(id,arg)
        self.type='IFCREGULARTIMESERIES'
        self.inverse={}
        self.TimeStep=None #IfcTimeMeasure
        self.Values=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCREGULARTIMESERIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREGULARTIMESERIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TimeStep= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Values= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREGULARTIMESERIES,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCREGULARTIMESERIES,self).toString()       
        line += integerToSPF(self.TimeStep)+','
        line += listParamToSPF(self.Values,idToSPF)+','

        return line
