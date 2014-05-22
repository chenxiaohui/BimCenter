#!/usr/bin/python
#coding=utf-8
#Filename:IfcRoundedEdgeFeature.py
import log
import common
from ifcedgefeature import IFCEDGEFEATURE

from utils import *

class IFCROUNDEDEDGEFEATURE(IFCEDGEFEATURE):
    """"""
    def __init__(self,id,arg):
        super(IFCROUNDEDEDGEFEATURE,self).__init__(id,arg)
        self.type='IFCROUNDEDEDGEFEATURE'
        self.inverse={}
        self.Radius=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCROUNDEDEDGEFEATURE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCROUNDEDEDGEFEATURE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Radius= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCROUNDEDEDGEFEATURE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCROUNDEDEDGEFEATURE,self).toString()       
        line += integerToSPF(self.Radius)+','

        return line
