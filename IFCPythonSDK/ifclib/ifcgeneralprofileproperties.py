#!/usr/bin/python
#coding=utf-8
#Filename:IfcGeneralProfileProperties.py
import log
import common
from ifcprofileproperties import IFCPROFILEPROPERTIES

from utils import *

class IFCGENERALPROFILEPROPERTIES(IFCPROFILEPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCGENERALPROFILEPROPERTIES,self).__init__(id,arg)
        self.type='IFCGENERALPROFILEPROPERTIES'
        self.inverse={}
        self.PhysicalWeight=None #IfcMassPerLengthMeasure
        self.Perimeter=None #IfcPositiveLengthMeasure
        self.MinimumPlateThickness=None #IfcPositiveLengthMeasure
        self.MaximumPlateThickness=None #IfcPositiveLengthMeasure
        self.CrossSectionArea=None #IfcAreaMeasure


    def load(self):
        """register inverses"""
        if not super(IFCGENERALPROFILEPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGENERALPROFILEPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PhysicalWeight= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Perimeter= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MinimumPlateThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MaximumPlateThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CrossSectionArea= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGENERALPROFILEPROPERTIES,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCGENERALPROFILEPROPERTIES,self).toString()       
        line += integerToSPF(self.PhysicalWeight)+','
        line += integerToSPF(self.Perimeter)+','
        line += integerToSPF(self.MinimumPlateThickness)+','
        line += integerToSPF(self.MaximumPlateThickness)+','
        line += integerToSPF(self.CrossSectionArea)+','

        return line
