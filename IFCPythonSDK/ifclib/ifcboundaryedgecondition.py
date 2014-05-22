#!/usr/bin/python
#coding=utf-8
#Filename:IfcBoundaryEdgeCondition.py
import log
import common
from ifcboundarycondition import IFCBOUNDARYCONDITION

from utils import *

class IFCBOUNDARYEDGECONDITION(IFCBOUNDARYCONDITION):
    """"""
    def __init__(self,id,arg):
        super(IFCBOUNDARYEDGECONDITION,self).__init__(id,arg)
        self.type='IFCBOUNDARYEDGECONDITION'
        self.inverse={}
        self.LinearStiffnessByLengthX=None #IfcModulusOfLinearSubgradeReactionMeasure
        self.LinearStiffnessByLengthY=None #IfcModulusOfLinearSubgradeReactionMeasure
        self.LinearStiffnessByLengthZ=None #IfcModulusOfLinearSubgradeReactionMeasure
        self.RotationalStiffnessByLengthX=None #IfcModulusOfRotationalSubgradeReactionMeasure
        self.RotationalStiffnessByLengthY=None #IfcModulusOfRotationalSubgradeReactionMeasure
        self.RotationalStiffnessByLengthZ=None #IfcModulusOfRotationalSubgradeReactionMeasure


    def load(self):
        """register inverses"""
        if not super(IFCBOUNDARYEDGECONDITION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBOUNDARYEDGECONDITION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearStiffnessByLengthX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearStiffnessByLengthY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearStiffnessByLengthZ= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RotationalStiffnessByLengthX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RotationalStiffnessByLengthY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RotationalStiffnessByLengthZ= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBOUNDARYEDGECONDITION,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCBOUNDARYEDGECONDITION,self).toString()       
        line += integerToSPF(self.LinearStiffnessByLengthX)+','
        line += integerToSPF(self.LinearStiffnessByLengthY)+','
        line += integerToSPF(self.LinearStiffnessByLengthZ)+','
        line += integerToSPF(self.RotationalStiffnessByLengthX)+','
        line += integerToSPF(self.RotationalStiffnessByLengthY)+','
        line += integerToSPF(self.RotationalStiffnessByLengthZ)+','

        return line
