#!/usr/bin/python
#coding=utf-8
#Filename:IfcElectricDistributionPoint.py
import log
import common
from ifcflowcontroller import IFCFLOWCONTROLLER

from utils import *

class IFCELECTRICDISTRIBUTIONPOINT(IFCFLOWCONTROLLER):
    """"""
    def __init__(self,id,arg):
        super(IFCELECTRICDISTRIBUTIONPOINT,self).__init__(id,arg)
        self.type='IFCELECTRICDISTRIBUTIONPOINT'
        self.inverse={}
        self.DistributionPointFunction=None #IfcElectricDistributionPointFunctionEnum
        self.UserDefinedFunction=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCELECTRICDISTRIBUTIONPOINT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELECTRICDISTRIBUTIONPOINT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DistributionPointFunction= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedFunction= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELECTRICDISTRIBUTIONPOINT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCELECTRICDISTRIBUTIONPOINT,self).toString()       
        line += typerefToSPF(self.DistributionPointFunction)+','
        line += strToSPF(self.UserDefinedFunction)+','

        return line
