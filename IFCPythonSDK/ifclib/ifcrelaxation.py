#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelaxation.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCRELAXATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCRELAXATION,self).__init__(id,arg)
        self.type='IFCRELAXATION'
        self.inverse={}
        self.RelaxationValue=None #IfcNormalisedRatioMeasure
        self.InitialStress=None #IfcNormalisedRatioMeasure


    def load(self):
        """register inverses"""
        if not super(IFCRELAXATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELAXATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelaxationValue= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InitialStress= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELAXATION,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELAXATION,self).toString()       
        line += integerToSPF(self.RelaxationValue)+','
        line += integerToSPF(self.InitialStress)+','

        return line
