#!/usr/bin/python
#coding=utf-8
#Filename:IfcReinforcingBar.py
import log
import common
from ifcreinforcingelement import IFCREINFORCINGELEMENT

from utils import *

class IFCREINFORCINGBAR(IFCREINFORCINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCREINFORCINGBAR,self).__init__(id,arg)
        self.type='IFCREINFORCINGBAR'
        self.inverse={}
        self.NominalDiameter=None #IfcPositiveLengthMeasure
        self.CrossSectionArea=None #IfcAreaMeasure
        self.BarLength=None #IfcPositiveLengthMeasure
        self.BarRole=None #IfcReinforcingBarRoleEnum
        self.BarSurface=None #IfcReinforcingBarSurfaceEnum


    def load(self):
        """register inverses"""
        if not super(IFCREINFORCINGBAR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREINFORCINGBAR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.NominalDiameter= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CrossSectionArea= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BarLength= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BarRole= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BarSurface= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREINFORCINGBAR,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCREINFORCINGBAR,self).toString()       
        line += integerToSPF(self.NominalDiameter)+','
        line += integerToSPF(self.CrossSectionArea)+','
        line += integerToSPF(self.BarLength)+','
        line += typerefToSPF(self.BarRole)+','
        line += typerefToSPF(self.BarSurface)+','

        return line
