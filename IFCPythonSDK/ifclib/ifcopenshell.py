#!/usr/bin/python
#coding=utf-8
#Filename:IfcOpenShell.py
import log
import common
from ifcconnectedfaceset import IFCCONNECTEDFACESET

from utils import *

class IFCOPENSHELL(IFCCONNECTEDFACESET):
    """"""
    def __init__(self,id,arg):
        super(IFCOPENSHELL,self).__init__(id,arg)
        self.type='IFCOPENSHELL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCOPENSHELL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCOPENSHELL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCOPENSHELL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCOPENSHELL,self).toString()       

        return line
