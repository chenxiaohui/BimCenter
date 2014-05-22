#!/usr/bin/python
#coding=utf-8
#Filename:IfcLightIntensityDistribution.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCLIGHTINTENSITYDISTRIBUTION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCLIGHTINTENSITYDISTRIBUTION,self).__init__(id,arg)
        self.type='IFCLIGHTINTENSITYDISTRIBUTION'
        self.inverse={}
        self.LightDistributionCurve=None #IfcLightDistributionCurveEnum
        self.DistributionData=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCLIGHTINTENSITYDISTRIBUTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLIGHTINTENSITYDISTRIBUTION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LightDistributionCurve= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DistributionData= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLIGHTINTENSITYDISTRIBUTION,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCLIGHTINTENSITYDISTRIBUTION,self).toString()       
        line += typerefToSPF(self.LightDistributionCurve)+','
        line += listParamToSPF(self.DistributionData,idToSPF)+','

        return line
