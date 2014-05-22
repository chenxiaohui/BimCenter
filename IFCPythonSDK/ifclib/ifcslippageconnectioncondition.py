#!/usr/bin/python
#coding=utf-8
#Filename:IfcSlippageConnectionCondition.py
import log
import common
from ifcstructuralconnectioncondition import IFCSTRUCTURALCONNECTIONCONDITION

from utils import *

class IFCSLIPPAGECONNECTIONCONDITION(IFCSTRUCTURALCONNECTIONCONDITION):
    """"""
    def __init__(self,id,arg):
        super(IFCSLIPPAGECONNECTIONCONDITION,self).__init__(id,arg)
        self.type='IFCSLIPPAGECONNECTIONCONDITION'
        self.inverse={}
        self.SlippageX=None #IfcLengthMeasure
        self.SlippageY=None #IfcLengthMeasure
        self.SlippageZ=None #IfcLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSLIPPAGECONNECTIONCONDITION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSLIPPAGECONNECTIONCONDITION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SlippageX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SlippageY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SlippageZ= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSLIPPAGECONNECTIONCONDITION,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCSLIPPAGECONNECTIONCONDITION,self).toString()       
        line += integerToSPF(self.SlippageX)+','
        line += integerToSPF(self.SlippageY)+','
        line += integerToSPF(self.SlippageZ)+','

        return line
