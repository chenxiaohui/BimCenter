#!/usr/bin/python
#coding=utf-8
#Filename:IfcLightDistributionData.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCLIGHTDISTRIBUTIONDATA(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCLIGHTDISTRIBUTIONDATA,self).__init__(id,arg)
        self.type='IFCLIGHTDISTRIBUTIONDATA'
        self.inverse={}
        self.MainPlaneAngle=None #IfcPlaneAngleMeasure
        self.SecondaryPlaneAngle=None #LIST
        self.LuminousIntensity=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCLIGHTDISTRIBUTIONDATA,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLIGHTDISTRIBUTIONDATA,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MainPlaneAngle= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SecondaryPlaneAngle= getIdListParam(arg,spfToInteger)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LuminousIntensity= getIdListParam(arg,spfToInteger)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLIGHTDISTRIBUTIONDATA,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCLIGHTDISTRIBUTIONDATA,self).toString()       
        line += integerToSPF(self.MainPlaneAngle)+','
        line += listParamToSPF(self.SecondaryPlaneAngle,integerToSPF)+','
        line += listParamToSPF(self.LuminousIntensity,integerToSPF)+','

        return line
