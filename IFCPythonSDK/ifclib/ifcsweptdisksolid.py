#!/usr/bin/python
#coding=utf-8
#Filename:IfcSweptDiskSolid.py
import log
import common
from ifcsolidmodel import IFCSOLIDMODEL

from utils import *

class IFCSWEPTDISKSOLID(IFCSOLIDMODEL):
    """"""
    def __init__(self,id,arg):
        super(IFCSWEPTDISKSOLID,self).__init__(id,arg)
        self.type='IFCSWEPTDISKSOLID'
        self.inverse={}
        self.Directrix=None #IfcCurve
        self.Radius=None #IfcPositiveLengthMeasure
        self.InnerRadius=None #IfcPositiveLengthMeasure
        self.StartParam=None #IfcParameterValue
        self.EndParam=None #IfcParameterValue


    def load(self):
        """register inverses"""
        if not super(IFCSWEPTDISKSOLID,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSWEPTDISKSOLID,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Directrix= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Radius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InnerRadius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.StartParam= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EndParam= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSWEPTDISKSOLID,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCSWEPTDISKSOLID,self).toString()       
        line += idToSPF(self.Directrix)+','
        line += integerToSPF(self.Radius)+','
        line += integerToSPF(self.InnerRadius)+','
        line += integerToSPF(self.StartParam)+','
        line += integerToSPF(self.EndParam)+','

        return line
