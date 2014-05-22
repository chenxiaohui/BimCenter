#!/usr/bin/python
#coding=utf-8
#Filename:IfcEnergyProperties.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCENERGYPROPERTIES(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCENERGYPROPERTIES,self).__init__(id,arg)
        self.type='IFCENERGYPROPERTIES'
        self.inverse={}
        self.EnergySequence=None #IfcEnergySequenceEnum
        self.UserDefinedEnergySequence=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCENERGYPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCENERGYPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EnergySequence= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedEnergySequence= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCENERGYPROPERTIES,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCENERGYPROPERTIES,self).toString()       
        line += typerefToSPF(self.EnergySequence)+','
        line += strToSPF(self.UserDefinedEnergySequence)+','

        return line
