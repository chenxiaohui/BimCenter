#!/usr/bin/python
#coding=utf-8
#Filename:IfcPointOnSurface.py
import log
import common
from ifcpoint import IFCPOINT

from utils import *

class IFCPOINTONSURFACE(IFCPOINT):
    """"""
    def __init__(self,id,arg):
        super(IFCPOINTONSURFACE,self).__init__(id,arg)
        self.type='IFCPOINTONSURFACE'
        self.inverse={}
        self.BasisSurface=None #IfcSurface
        self.PointParameterU=None #IfcParameterValue
        self.PointParameterV=None #IfcParameterValue


    def load(self):
        """register inverses"""
        if not super(IFCPOINTONSURFACE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPOINTONSURFACE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BasisSurface= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PointParameterU= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PointParameterV= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPOINTONSURFACE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCPOINTONSURFACE,self).toString()       
        line += idToSPF(self.BasisSurface)+','
        line += integerToSPF(self.PointParameterU)+','
        line += integerToSPF(self.PointParameterV)+','

        return line
