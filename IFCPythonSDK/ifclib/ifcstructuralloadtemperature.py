#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLoadTemperature.py
import log
import common
from ifcstructuralloadstatic import IFCSTRUCTURALLOADSTATIC

from utils import *

class IFCSTRUCTURALLOADTEMPERATURE(IFCSTRUCTURALLOADSTATIC):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLOADTEMPERATURE,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLOADTEMPERATURE'
        self.inverse={}
        self.DeltaT_Constant=None #IfcThermodynamicTemperatureMeasure
        self.DeltaT_Y=None #IfcThermodynamicTemperatureMeasure
        self.DeltaT_Z=None #IfcThermodynamicTemperatureMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLOADTEMPERATURE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLOADTEMPERATURE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DeltaT_Constant= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DeltaT_Y= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DeltaT_Z= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALLOADTEMPERATURE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLOADTEMPERATURE,self).toString()       
        line += integerToSPF(self.DeltaT_Constant)+','
        line += integerToSPF(self.DeltaT_Y)+','
        line += integerToSPF(self.DeltaT_Z)+','

        return line
