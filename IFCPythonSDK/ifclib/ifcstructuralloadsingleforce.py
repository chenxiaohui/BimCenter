#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLoadSingleForce.py
import log
import common
from ifcstructuralloadstatic import IFCSTRUCTURALLOADSTATIC

from utils import *

class IFCSTRUCTURALLOADSINGLEFORCE(IFCSTRUCTURALLOADSTATIC):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLOADSINGLEFORCE,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLOADSINGLEFORCE'
        self.inverse={}
        self.ForceX=None #IfcForceMeasure
        self.ForceY=None #IfcForceMeasure
        self.ForceZ=None #IfcForceMeasure
        self.MomentX=None #IfcTorqueMeasure
        self.MomentY=None #IfcTorqueMeasure
        self.MomentZ=None #IfcTorqueMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLOADSINGLEFORCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLOADSINGLEFORCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ForceX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ForceY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ForceZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MomentX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MomentY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MomentZ= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALLOADSINGLEFORCE,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLOADSINGLEFORCE,self).toString()       
        line += integerToSPF(self.ForceX)+','
        line += integerToSPF(self.ForceY)+','
        line += integerToSPF(self.ForceZ)+','
        line += integerToSPF(self.MomentX)+','
        line += integerToSPF(self.MomentY)+','
        line += integerToSPF(self.MomentZ)+','

        return line
