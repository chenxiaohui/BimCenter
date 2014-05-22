#!/usr/bin/python
#coding=utf-8
#Filename:IfcEdgeFeature.py
import log
import common
from ifcfeatureelementsubtraction import IFCFEATUREELEMENTSUBTRACTION

from utils import *

class IFCEDGEFEATURE(IFCFEATUREELEMENTSUBTRACTION):
    """"""
    def __init__(self,id,arg):
        super(IFCEDGEFEATURE,self).__init__(id,arg)
        self.type='IFCEDGEFEATURE'
        self.inverse={}
        self.FeatureLength=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCEDGEFEATURE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEDGEFEATURE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FeatureLength= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEDGEFEATURE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCEDGEFEATURE,self).toString()       
        line += integerToSPF(self.FeatureLength)+','

        return line
