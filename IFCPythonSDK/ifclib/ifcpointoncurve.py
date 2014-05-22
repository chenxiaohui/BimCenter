#!/usr/bin/python
#coding=utf-8
#Filename:IfcPointOnCurve.py
import log
import common
from ifcpoint import IFCPOINT

from utils import *

class IFCPOINTONCURVE(IFCPOINT):
    """"""
    def __init__(self,id,arg):
        super(IFCPOINTONCURVE,self).__init__(id,arg)
        self.type='IFCPOINTONCURVE'
        self.inverse={}
        self.BasisCurve=None #IfcCurve
        self.PointParameter=None #IfcParameterValue


    def load(self):
        """register inverses"""
        if not super(IFCPOINTONCURVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPOINTONCURVE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BasisCurve= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PointParameter= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPOINTONCURVE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPOINTONCURVE,self).toString()       
        line += idToSPF(self.BasisCurve)+','
        line += integerToSPF(self.PointParameter)+','

        return line
