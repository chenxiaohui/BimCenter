#!/usr/bin/python
#coding=utf-8
#Filename:IfcEnergyConversionDevice.py
import log
import common
from ifcdistributionflowelement import IFCDISTRIBUTIONFLOWELEMENT

from utils import *

class IFCENERGYCONVERSIONDEVICE(IFCDISTRIBUTIONFLOWELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCENERGYCONVERSIONDEVICE,self).__init__(id,arg)
        self.type='IFCENERGYCONVERSIONDEVICE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCENERGYCONVERSIONDEVICE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCENERGYCONVERSIONDEVICE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCENERGYCONVERSIONDEVICE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCENERGYCONVERSIONDEVICE,self).toString()       

        return line
