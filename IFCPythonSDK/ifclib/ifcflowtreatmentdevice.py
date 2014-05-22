#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowTreatmentDevice.py
import log
import common
from ifcdistributionflowelement import IFCDISTRIBUTIONFLOWELEMENT

from utils import *

class IFCFLOWTREATMENTDEVICE(IFCDISTRIBUTIONFLOWELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWTREATMENTDEVICE,self).__init__(id,arg)
        self.type='IFCFLOWTREATMENTDEVICE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWTREATMENTDEVICE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWTREATMENTDEVICE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWTREATMENTDEVICE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWTREATMENTDEVICE,self).toString()       

        return line
