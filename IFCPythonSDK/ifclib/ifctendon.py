#!/usr/bin/python
#coding=utf-8
#Filename:IfcTendon.py
import log
import common
from ifcreinforcingelement import IFCREINFORCINGELEMENT

from utils import *

class IFCTENDON(IFCREINFORCINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCTENDON,self).__init__(id,arg)
        self.type='IFCTENDON'
        self.inverse={}
        self.PredefinedType=None #IfcTendonTypeEnum
        self.NominalDiameter=None #IfcPositiveLengthMeasure
        self.CrossSectionArea=None #IfcAreaMeasure
        self.TensionForce=None #IfcForceMeasure
        self.PreStress=None #IfcPressureMeasure
        self.FrictionCoefficient=None #IfcNormalisedRatioMeasure
        self.AnchorageSlip=None #IfcPositiveLengthMeasure
        self.MinCurvatureRadius=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCTENDON,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTENDON,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.NominalDiameter= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CrossSectionArea= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TensionForce= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PreStress= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FrictionCoefficient= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AnchorageSlip= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MinCurvatureRadius= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTENDON,self).getAttrCount()+8

    def toString(self):
        """"""
        line=super(IFCTENDON,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','
        line += integerToSPF(self.NominalDiameter)+','
        line += integerToSPF(self.CrossSectionArea)+','
        line += integerToSPF(self.TensionForce)+','
        line += integerToSPF(self.PreStress)+','
        line += integerToSPF(self.FrictionCoefficient)+','
        line += integerToSPF(self.AnchorageSlip)+','
        line += integerToSPF(self.MinCurvatureRadius)+','

        return line
