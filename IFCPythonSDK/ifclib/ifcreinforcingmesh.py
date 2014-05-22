#!/usr/bin/python
#coding=utf-8
#Filename:IfcReinforcingMesh.py
import log
import common
from ifcreinforcingelement import IFCREINFORCINGELEMENT

from utils import *

class IFCREINFORCINGMESH(IFCREINFORCINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCREINFORCINGMESH,self).__init__(id,arg)
        self.type='IFCREINFORCINGMESH'
        self.inverse={}
        self.MeshLength=None #IfcPositiveLengthMeasure
        self.MeshWidth=None #IfcPositiveLengthMeasure
        self.LongitudinalBarNominalDiameter=None #IfcPositiveLengthMeasure
        self.TransverseBarNominalDiameter=None #IfcPositiveLengthMeasure
        self.LongitudinalBarCrossSectionArea=None #IfcAreaMeasure
        self.TransverseBarCrossSectionArea=None #IfcAreaMeasure
        self.LongitudinalBarSpacing=None #IfcPositiveLengthMeasure
        self.TransverseBarSpacing=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCREINFORCINGMESH,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREINFORCINGMESH,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MeshLength= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MeshWidth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LongitudinalBarNominalDiameter= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TransverseBarNominalDiameter= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LongitudinalBarCrossSectionArea= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TransverseBarCrossSectionArea= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LongitudinalBarSpacing= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TransverseBarSpacing= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREINFORCINGMESH,self).getAttrCount()+8

    def toString(self):
        """"""
        line=super(IFCREINFORCINGMESH,self).toString()       
        line += integerToSPF(self.MeshLength)+','
        line += integerToSPF(self.MeshWidth)+','
        line += integerToSPF(self.LongitudinalBarNominalDiameter)+','
        line += integerToSPF(self.TransverseBarNominalDiameter)+','
        line += integerToSPF(self.LongitudinalBarCrossSectionArea)+','
        line += integerToSPF(self.TransverseBarCrossSectionArea)+','
        line += integerToSPF(self.LongitudinalBarSpacing)+','
        line += integerToSPF(self.TransverseBarSpacing)+','

        return line
