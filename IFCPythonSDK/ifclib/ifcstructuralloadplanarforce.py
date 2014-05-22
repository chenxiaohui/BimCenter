#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLoadPlanarForce.py
import log
import common
from ifcstructuralloadstatic import IFCSTRUCTURALLOADSTATIC

from utils import *

class IFCSTRUCTURALLOADPLANARFORCE(IFCSTRUCTURALLOADSTATIC):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLOADPLANARFORCE,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLOADPLANARFORCE'
        self.inverse={}
        self.PlanarForceX=None #IfcPlanarForceMeasure
        self.PlanarForceY=None #IfcPlanarForceMeasure
        self.PlanarForceZ=None #IfcPlanarForceMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLOADPLANARFORCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLOADPLANARFORCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PlanarForceX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PlanarForceY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PlanarForceZ= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALLOADPLANARFORCE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLOADPLANARFORCE,self).toString()       
        line += integerToSPF(self.PlanarForceX)+','
        line += integerToSPF(self.PlanarForceY)+','
        line += integerToSPF(self.PlanarForceZ)+','

        return line
