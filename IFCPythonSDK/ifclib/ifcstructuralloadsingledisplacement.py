#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLoadSingleDisplacement.py
import log
import common
from ifcstructuralloadstatic import IFCSTRUCTURALLOADSTATIC

from utils import *

class IFCSTRUCTURALLOADSINGLEDISPLACEMENT(IFCSTRUCTURALLOADSTATIC):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLOADSINGLEDISPLACEMENT,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLOADSINGLEDISPLACEMENT'
        self.inverse={}
        self.DisplacementX=None #IfcLengthMeasure
        self.DisplacementY=None #IfcLengthMeasure
        self.DisplacementZ=None #IfcLengthMeasure
        self.RotationalDisplacementRX=None #IfcPlaneAngleMeasure
        self.RotationalDisplacementRY=None #IfcPlaneAngleMeasure
        self.RotationalDisplacementRZ=None #IfcPlaneAngleMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLOADSINGLEDISPLACEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLOADSINGLEDISPLACEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DisplacementX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DisplacementY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DisplacementZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RotationalDisplacementRX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RotationalDisplacementRY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RotationalDisplacementRZ= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALLOADSINGLEDISPLACEMENT,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLOADSINGLEDISPLACEMENT,self).toString()       
        line += integerToSPF(self.DisplacementX)+','
        line += integerToSPF(self.DisplacementY)+','
        line += integerToSPF(self.DisplacementZ)+','
        line += integerToSPF(self.RotationalDisplacementRX)+','
        line += integerToSPF(self.RotationalDisplacementRY)+','
        line += integerToSPF(self.RotationalDisplacementRZ)+','

        return line
