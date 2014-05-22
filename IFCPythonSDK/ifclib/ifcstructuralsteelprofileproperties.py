#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralSteelProfileProperties.py
import log
import common
from ifcstructuralprofileproperties import IFCSTRUCTURALPROFILEPROPERTIES

from utils import *

class IFCSTRUCTURALSTEELPROFILEPROPERTIES(IFCSTRUCTURALPROFILEPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALSTEELPROFILEPROPERTIES,self).__init__(id,arg)
        self.type='IFCSTRUCTURALSTEELPROFILEPROPERTIES'
        self.inverse={}
        self.ShearAreaZ=None #IfcAreaMeasure
        self.ShearAreaY=None #IfcAreaMeasure
        self.PlasticShapeFactorY=None #IfcPositiveRatioMeasure
        self.PlasticShapeFactorZ=None #IfcPositiveRatioMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALSTEELPROFILEPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALSTEELPROFILEPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShearAreaZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShearAreaY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PlasticShapeFactorY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PlasticShapeFactorZ= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALSTEELPROFILEPROPERTIES,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALSTEELPROFILEPROPERTIES,self).toString()       
        line += integerToSPF(self.ShearAreaZ)+','
        line += integerToSPF(self.ShearAreaY)+','
        line += integerToSPF(self.PlasticShapeFactorY)+','
        line += integerToSPF(self.PlasticShapeFactorZ)+','

        return line
