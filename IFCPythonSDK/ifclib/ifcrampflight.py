#!/usr/bin/python
#coding=utf-8
#Filename:IfcRampFlight.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCRAMPFLIGHT(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCRAMPFLIGHT,self).__init__(id,arg)
        self.type='IFCRAMPFLIGHT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCRAMPFLIGHT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRAMPFLIGHT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRAMPFLIGHT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCRAMPFLIGHT,self).toString()       

        return line
