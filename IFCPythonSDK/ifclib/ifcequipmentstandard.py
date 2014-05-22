#!/usr/bin/python
#coding=utf-8
#Filename:IfcEquipmentStandard.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCEQUIPMENTSTANDARD(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCEQUIPMENTSTANDARD,self).__init__(id,arg)
        self.type='IFCEQUIPMENTSTANDARD'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCEQUIPMENTSTANDARD,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEQUIPMENTSTANDARD,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEQUIPMENTSTANDARD,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCEQUIPMENTSTANDARD,self).toString()       

        return line
