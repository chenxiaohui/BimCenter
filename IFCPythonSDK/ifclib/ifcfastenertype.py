#!/usr/bin/python
#coding=utf-8
#Filename:IfcFastenerType.py
import log
import common
from ifcelementcomponenttype import IFCELEMENTCOMPONENTTYPE

from utils import *

class IFCFASTENERTYPE(IFCELEMENTCOMPONENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFASTENERTYPE,self).__init__(id,arg)
        self.type='IFCFASTENERTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFASTENERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFASTENERTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFASTENERTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFASTENERTYPE,self).toString()       

        return line
