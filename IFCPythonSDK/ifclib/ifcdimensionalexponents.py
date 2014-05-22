#!/usr/bin/python
#coding=utf-8
#Filename:IfcDimensionalExponents.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCDIMENSIONALEXPONENTS(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCDIMENSIONALEXPONENTS,self).__init__(id,arg)
        self.type='IFCDIMENSIONALEXPONENTS'
        self.inverse={}
        self.LengthExponent=None #INTEGER
        self.MassExponent=None #INTEGER
        self.TimeExponent=None #INTEGER
        self.ElectricCurrentExponent=None #INTEGER
        self.ThermodynamicTemperatureExponent=None #INTEGER
        self.AmountOfSubstanceExponent=None #INTEGER
        self.LuminousIntensityExponent=None #INTEGER


    def load(self):
        """register inverses"""
        if not super(IFCDIMENSIONALEXPONENTS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDIMENSIONALEXPONENTS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LengthExponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MassExponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TimeExponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ElectricCurrentExponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThermodynamicTemperatureExponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AmountOfSubstanceExponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LuminousIntensityExponent= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDIMENSIONALEXPONENTS,self).getAttrCount()+7

    def toString(self):
        """"""
        line=super(IFCDIMENSIONALEXPONENTS,self).toString()       
        line += integerToSPF(self.LengthExponent)+','
        line += integerToSPF(self.MassExponent)+','
        line += integerToSPF(self.TimeExponent)+','
        line += integerToSPF(self.ElectricCurrentExponent)+','
        line += integerToSPF(self.ThermodynamicTemperatureExponent)+','
        line += integerToSPF(self.AmountOfSubstanceExponent)+','
        line += integerToSPF(self.LuminousIntensityExponent)+','

        return line
