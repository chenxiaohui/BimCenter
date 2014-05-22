#!/usr/bin/python
#coding=utf-8
#Filename:IfcChamferEdgeFeature.py
import log
import common
from ifcedgefeature import IFCEDGEFEATURE

from utils import *

class IFCCHAMFEREDGEFEATURE(IFCEDGEFEATURE):
    """"""
    def __init__(self,id,arg):
        super(IFCCHAMFEREDGEFEATURE,self).__init__(id,arg)
        self.type='IFCCHAMFEREDGEFEATURE'
        self.inverse={}
        self.Width=None #IfcPositiveLengthMeasure
        self.Height=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCHAMFEREDGEFEATURE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCHAMFEREDGEFEATURE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Width= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Height= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCHAMFEREDGEFEATURE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCHAMFEREDGEFEATURE,self).toString()       
        line += integerToSPF(self.Width)+','
        line += integerToSPF(self.Height)+','

        return line
