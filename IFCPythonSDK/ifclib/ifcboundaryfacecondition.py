#!/usr/bin/python
#coding=utf-8
#Filename:IfcBoundaryFaceCondition.py
import log
import common
from ifcboundarycondition import IFCBOUNDARYCONDITION

from utils import *

class IFCBOUNDARYFACECONDITION(IFCBOUNDARYCONDITION):
    """"""
    def __init__(self,id,arg):
        super(IFCBOUNDARYFACECONDITION,self).__init__(id,arg)
        self.type='IFCBOUNDARYFACECONDITION'
        self.inverse={}
        self.LinearStiffnessByAreaX=None #IfcModulusOfSubgradeReactionMeasure
        self.LinearStiffnessByAreaY=None #IfcModulusOfSubgradeReactionMeasure
        self.LinearStiffnessByAreaZ=None #IfcModulusOfSubgradeReactionMeasure


    def load(self):
        """register inverses"""
        if not super(IFCBOUNDARYFACECONDITION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBOUNDARYFACECONDITION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearStiffnessByAreaX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearStiffnessByAreaY= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LinearStiffnessByAreaZ= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBOUNDARYFACECONDITION,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCBOUNDARYFACECONDITION,self).toString()       
        line += integerToSPF(self.LinearStiffnessByAreaX)+','
        line += integerToSPF(self.LinearStiffnessByAreaY)+','
        line += integerToSPF(self.LinearStiffnessByAreaZ)+','

        return line
