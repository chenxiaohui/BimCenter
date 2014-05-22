#!/usr/bin/python
#coding=utf-8
#Filename:IfcBuildingStorey.py
import log
import common
from ifcspatialstructureelement import IFCSPATIALSTRUCTUREELEMENT

from utils import *

class IFCBUILDINGSTOREY(IFCSPATIALSTRUCTUREELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCBUILDINGSTOREY,self).__init__(id,arg)
        self.type='IFCBUILDINGSTOREY'
        self.inverse={}
        self.Elevation=None #IfcLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCBUILDINGSTOREY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBUILDINGSTOREY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Elevation= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBUILDINGSTOREY,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCBUILDINGSTOREY,self).toString()       
        line += integerToSPF(self.Elevation)+','

        return line
