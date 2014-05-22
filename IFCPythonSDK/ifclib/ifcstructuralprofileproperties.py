#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralProfileProperties.py
import log
import common
from ifcgeneralprofileproperties import IFCGENERALPROFILEPROPERTIES

from utils import *

class IFCSTRUCTURALPROFILEPROPERTIES(IFCGENERALPROFILEPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALPROFILEPROPERTIES,self).__init__(id,arg)
        self.type='IFCSTRUCTURALPROFILEPROPERTIES'
        self.inverse={}
        self.TorsionalConstantX=None #IfcMomentOfInertiaMeasure
        self.MomentOfInertiaYZ=None #IfcMomentOfInertiaMeasure
        self.MomentOfInertiaY=None #IfcMomentOfInertiaMeasure
        self.MomentOfInertiaZ=None #IfcMomentOfInertiaMeasure
        self.WarpingConstant=None #IfcWarpingConstantMeasure
        self.ShearCentreZ=None #IfcLengthMeasure
        self.ShearCentreY=None #IfcLengthMeasure
        self.ShearDeformationAreaZ=None #IfcAreaMeasure
        self.ShearDeformationAreaY=None #IfcAreaMeasure
        self.MaximumSectionModulusY=None #IfcSectionModulusMeasure
        self.MinimumSectionModulusY=None #IfcSectionModulusMeasure
        self.MaximumSectionModulusZ=None #IfcSectionModulusMeasure
        self.MinimumSectionModulusZ=None #IfcSectionModulusMeasure
        self.TorsionalSectionModulus=None #IfcSectionModulusMeasure
        self.CentreOfGravityInX=None #IfcLengthMeasure
        self.CentreOfGravityInY=None #IfcLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALPROFILEPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALPROFILEPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TorsionalConstantX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MomentOfInertiaYZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MomentOfInertiaY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MomentOfInertiaZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WarpingConstant= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShearCentreZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShearCentreY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShearDeformationAreaZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShearDeformationAreaY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MaximumSectionModulusY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MinimumSectionModulusY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MaximumSectionModulusZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MinimumSectionModulusZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TorsionalSectionModulus= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CentreOfGravityInX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CentreOfGravityInY= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALPROFILEPROPERTIES,self).getAttrCount()+16

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALPROFILEPROPERTIES,self).toString()       
        line += integerToSPF(self.TorsionalConstantX)+','
        line += integerToSPF(self.MomentOfInertiaYZ)+','
        line += integerToSPF(self.MomentOfInertiaY)+','
        line += integerToSPF(self.MomentOfInertiaZ)+','
        line += integerToSPF(self.WarpingConstant)+','
        line += integerToSPF(self.ShearCentreZ)+','
        line += integerToSPF(self.ShearCentreY)+','
        line += integerToSPF(self.ShearDeformationAreaZ)+','
        line += integerToSPF(self.ShearDeformationAreaY)+','
        line += integerToSPF(self.MaximumSectionModulusY)+','
        line += integerToSPF(self.MinimumSectionModulusY)+','
        line += integerToSPF(self.MaximumSectionModulusZ)+','
        line += integerToSPF(self.MinimumSectionModulusZ)+','
        line += integerToSPF(self.TorsionalSectionModulus)+','
        line += integerToSPF(self.CentreOfGravityInX)+','
        line += integerToSPF(self.CentreOfGravityInY)+','

        return line
