#!/usr/bin/python
#coding=utf-8
#Filename:IfcEquipmentElement.py
import log
import common
from ifcelement import IFCELEMENT

from utils import *

class IFCEQUIPMENTELEMENT(IFCELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCEQUIPMENTELEMENT,self).__init__(id,arg)
        self.type='IFCEQUIPMENTELEMENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCEQUIPMENTELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEQUIPMENTELEMENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEQUIPMENTELEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCEQUIPMENTELEMENT,self).toString()       

        return line
