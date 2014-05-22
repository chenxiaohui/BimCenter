#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLoadLinearForce.py
import log
import common
from ifcstructuralloadstatic import IFCSTRUCTURALLOADSTATIC

from utils import *

class IFCSTRUCTURALLOADLINEARFORCE(IFCSTRUCTURALLOADSTATIC):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLOADLINEARFORCE,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLOADLINEARFORCE'
        self.inverse={}
        self.LinearForceX=None #IfcLinearForceMeasure
        self.LinearForceY=None #IfcLinearForceMeasure
        self.LinearForceZ=None #IfcLinearForceMeasure
        self.LinearMomentX=None #IfcLinearMomentMeasure
        self.LinearMomentY=None #IfcLinearMomentMeasure
        self.LinearMomentZ=None #IfcLinearMomentMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLOADLINEARFORCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLOADLINEARFORCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearForceX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearForceY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearForceZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearMomentX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearMomentY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearMomentZ= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALLOADLINEARFORCE,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLOADLINEARFORCE,self).toString()       
        line += integerToSPF(self.LinearForceX)+','
        line += integerToSPF(self.LinearForceY)+','
        line += integerToSPF(self.LinearForceZ)+','
        line += integerToSPF(self.LinearMomentX)+','
        line += integerToSPF(self.LinearMomentY)+','
        line += integerToSPF(self.LinearMomentZ)+','

        return line
