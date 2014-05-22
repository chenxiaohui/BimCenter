#!/usr/bin/python
#coding=utf-8
#Filename:IfcMetric.py
import log
import common
from ifcconstraint import IFCCONSTRAINT

from utils import *

class IFCMETRIC(IFCCONSTRAINT):
    """"""
    def __init__(self,id,arg):
        super(IFCMETRIC,self).__init__(id,arg)
        self.type='IFCMETRIC'
        self.inverse={}
        self.Benchmark=None #IfcBenchmarkEnum
        self.ValueSource=None #IfcLabel
        self.DataValue=None #IfcMetricValueSelect


    def load(self):
        """register inverses"""
        if not super(IFCMETRIC,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMETRIC,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Benchmark= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ValueSource= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DataValue= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMETRIC,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCMETRIC,self).toString()       
        line += typerefToSPF(self.Benchmark)+','
        line += strToSPF(self.ValueSource)+','
        line += typerefToSPF(self.DataValue)+','

        return line
