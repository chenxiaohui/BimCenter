#!/usr/bin/python
#coding=utf-8
#Filename:IfcObjective.py
import log
import common
from ifcconstraint import IFCCONSTRAINT

from utils import *

class IFCOBJECTIVE(IFCCONSTRAINT):
    """"""
    def __init__(self,id,arg):
        super(IFCOBJECTIVE,self).__init__(id,arg)
        self.type='IFCOBJECTIVE'
        self.inverse={}
        self.BenchmarkValues=None #IfcMetric
        self.ResultValues=None #IfcMetric
        self.ObjectiveQualifier=None #IfcObjectiveEnum
        self.UserDefinedQualifier=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCOBJECTIVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCOBJECTIVE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BenchmarkValues= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ResultValues= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ObjectiveQualifier= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedQualifier= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCOBJECTIVE,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCOBJECTIVE,self).toString()       
        line += idToSPF(self.BenchmarkValues)+','
        line += idToSPF(self.ResultValues)+','
        line += typerefToSPF(self.ObjectiveQualifier)+','
        line += strToSPF(self.UserDefinedQualifier)+','

        return line
