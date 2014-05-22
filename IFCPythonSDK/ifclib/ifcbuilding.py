#!/usr/bin/python
#coding=utf-8
#Filename:IfcBuilding.py
import log
import common
from ifcspatialstructureelement import IFCSPATIALSTRUCTUREELEMENT

from utils import *

class IFCBUILDING(IFCSPATIALSTRUCTUREELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCBUILDING,self).__init__(id,arg)
        self.type='IFCBUILDING'
        self.inverse={}
        self.ElevationOfRefHeight=None #IfcLengthMeasure
        self.ElevationOfTerrain=None #IfcLengthMeasure
        self.BuildingAddress=None #IfcPostalAddress


    def load(self):
        """register inverses"""
        if not super(IFCBUILDING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBUILDING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ElevationOfRefHeight= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ElevationOfTerrain= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BuildingAddress= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBUILDING,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCBUILDING,self).toString()       
        line += integerToSPF(self.ElevationOfRefHeight)+','
        line += integerToSPF(self.ElevationOfTerrain)+','
        line += idToSPF(self.BuildingAddress)+','

        return line
