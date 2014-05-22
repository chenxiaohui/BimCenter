#!/usr/bin/python
#coding=utf-8
#Filename:IfcBoundaryNodeCondition.py
import log
import common
from ifcboundarycondition import IFCBOUNDARYCONDITION

from utils import *

class IFCBOUNDARYNODECONDITION(IFCBOUNDARYCONDITION):
    """"""
    def __init__(self,id,arg):
        super(IFCBOUNDARYNODECONDITION,self).__init__(id,arg)
        self.type='IFCBOUNDARYNODECONDITION'
        self.inverse={}
        self.LinearStiffnessX=None #IfcLinearStiffnessMeasure
        self.LinearStiffnessY=None #IfcLinearStiffnessMeasure
        self.LinearStiffnessZ=None #IfcLinearStiffnessMeasure
        self.RotationalStiffnessX=None #IfcRotationalStiffnessMeasure
        self.RotationalStiffnessY=None #IfcRotationalStiffnessMeasure
        self.RotationalStiffnessZ=None #IfcRotationalStiffnessMeasure


    def load(self):
        """register inverses"""
        if not super(IFCBOUNDARYNODECONDITION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBOUNDARYNODECONDITION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearStiffnessX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearStiffnessY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearStiffnessZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RotationalStiffnessX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RotationalStiffnessY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RotationalStiffnessZ= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBOUNDARYNODECONDITION,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCBOUNDARYNODECONDITION,self).toString()       
        line += integerToSPF(self.LinearStiffnessX)+','
        line += integerToSPF(self.LinearStiffnessY)+','
        line += integerToSPF(self.LinearStiffnessZ)+','
        line += integerToSPF(self.RotationalStiffnessX)+','
        line += integerToSPF(self.RotationalStiffnessY)+','
        line += integerToSPF(self.RotationalStiffnessZ)+','

        return line
