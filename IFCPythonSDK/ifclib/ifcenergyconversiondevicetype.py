#!/usr/bin/python
#coding=utf-8
#Filename:IfcEnergyConversionDeviceType.py
import log
import common
from ifcdistributionflowelementtype import IFCDISTRIBUTIONFLOWELEMENTTYPE

from utils import *

class IFCENERGYCONVERSIONDEVICETYPE(IFCDISTRIBUTIONFLOWELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCENERGYCONVERSIONDEVICETYPE,self).__init__(id,arg)
        self.type='IFCENERGYCONVERSIONDEVICETYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCENERGYCONVERSIONDEVICETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCENERGYCONVERSIONDEVICETYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCENERGYCONVERSIONDEVICETYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCENERGYCONVERSIONDEVICETYPE,self).toString()       

        return line
