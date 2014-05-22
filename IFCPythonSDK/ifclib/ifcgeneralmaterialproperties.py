#!/usr/bin/python
#coding=utf-8
#Filename:IfcGeneralMaterialProperties.py
import log
import common
from ifcmaterialproperties import IFCMATERIALPROPERTIES

from utils import *

class IFCGENERALMATERIALPROPERTIES(IFCMATERIALPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCGENERALMATERIALPROPERTIES,self).__init__(id,arg)
        self.type='IFCGENERALMATERIALPROPERTIES'
        self.inverse={}
        self.MolecularWeight=None #IfcMolecularWeightMeasure
        self.Porosity=None #IfcNormalisedRatioMeasure
        self.MassDensity=None #IfcMassDensityMeasure


    def load(self):
        """register inverses"""
        if not super(IFCGENERALMATERIALPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGENERALMATERIALPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MolecularWeight= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Porosity= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MassDensity= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGENERALMATERIALPROPERTIES,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCGENERALMATERIALPROPERTIES,self).toString()       
        line += integerToSPF(self.MolecularWeight)+','
        line += integerToSPF(self.Porosity)+','
        line += integerToSPF(self.MassDensity)+','

        return line
