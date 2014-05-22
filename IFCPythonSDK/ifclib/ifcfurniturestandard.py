#!/usr/bin/python
#coding=utf-8
#Filename:IfcFurnitureStandard.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCFURNITURESTANDARD(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCFURNITURESTANDARD,self).__init__(id,arg)
        self.type='IFCFURNITURESTANDARD'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFURNITURESTANDARD,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFURNITURESTANDARD,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFURNITURESTANDARD,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFURNITURESTANDARD,self).toString()       

        return line
