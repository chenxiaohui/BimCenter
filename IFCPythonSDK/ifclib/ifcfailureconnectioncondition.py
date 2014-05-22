#!/usr/bin/python
#coding=utf-8
#Filename:IfcFailureConnectionCondition.py
import log
import common
from ifcstructuralconnectioncondition import IFCSTRUCTURALCONNECTIONCONDITION

from utils import *

class IFCFAILURECONNECTIONCONDITION(IFCSTRUCTURALCONNECTIONCONDITION):
    """"""
    def __init__(self,id,arg):
        super(IFCFAILURECONNECTIONCONDITION,self).__init__(id,arg)
        self.type='IFCFAILURECONNECTIONCONDITION'
        self.inverse={}
        self.TensionFailureX=None #IfcForceMeasure
        self.TensionFailureY=None #IfcForceMeasure
        self.TensionFailureZ=None #IfcForceMeasure
        self.CompressionFailureX=None #IfcForceMeasure
        self.CompressionFailureY=None #IfcForceMeasure
        self.CompressionFailureZ=None #IfcForceMeasure


    def load(self):
        """register inverses"""
        if not super(IFCFAILURECONNECTIONCONDITION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFAILURECONNECTIONCONDITION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TensionFailureX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TensionFailureY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TensionFailureZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CompressionFailureX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CompressionFailureY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CompressionFailureZ= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFAILURECONNECTIONCONDITION,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCFAILURECONNECTIONCONDITION,self).toString()       
        line += integerToSPF(self.TensionFailureX)+','
        line += integerToSPF(self.TensionFailureY)+','
        line += integerToSPF(self.TensionFailureZ)+','
        line += integerToSPF(self.CompressionFailureX)+','
        line += integerToSPF(self.CompressionFailureY)+','
        line += integerToSPF(self.CompressionFailureZ)+','

        return line
