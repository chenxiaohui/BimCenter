#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowTreatmentDeviceType.py
import log
import common
from ifcdistributionflowelementtype import IFCDISTRIBUTIONFLOWELEMENTTYPE

from utils import *

class IFCFLOWTREATMENTDEVICETYPE(IFCDISTRIBUTIONFLOWELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWTREATMENTDEVICETYPE,self).__init__(id,arg)
        self.type='IFCFLOWTREATMENTDEVICETYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWTREATMENTDEVICETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWTREATMENTDEVICETYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWTREATMENTDEVICETYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWTREATMENTDEVICETYPE,self).toString()       

        return line
