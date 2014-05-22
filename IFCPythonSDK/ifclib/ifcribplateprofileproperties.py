#!/usr/bin/python
#coding=utf-8
#Filename:IfcRibPlateProfileProperties.py
import log
import common
from ifcprofileproperties import IFCPROFILEPROPERTIES

from utils import *

class IFCRIBPLATEPROFILEPROPERTIES(IFCPROFILEPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCRIBPLATEPROFILEPROPERTIES,self).__init__(id,arg)
        self.type='IFCRIBPLATEPROFILEPROPERTIES'
        self.inverse={}
        self.Thickness=None #IfcPositiveLengthMeasure
        self.RibHeight=None #IfcPositiveLengthMeasure
        self.RibWidth=None #IfcPositiveLengthMeasure
        self.RibSpacing=None #IfcPositiveLengthMeasure
        self.Direction=None #IfcRibPlateDirectionEnum


    def load(self):
        """register inverses"""
        if not super(IFCRIBPLATEPROFILEPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRIBPLATEPROFILEPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Thickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RibHeight= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RibWidth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RibSpacing= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Direction= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRIBPLATEPROFILEPROPERTIES,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCRIBPLATEPROFILEPROPERTIES,self).toString()       
        line += integerToSPF(self.Thickness)+','
        line += integerToSPF(self.RibHeight)+','
        line += integerToSPF(self.RibWidth)+','
        line += integerToSPF(self.RibSpacing)+','
        line += typerefToSPF(self.Direction)+','

        return line
