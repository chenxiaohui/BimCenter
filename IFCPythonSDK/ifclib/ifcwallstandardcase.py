#!/usr/bin/python
#coding=utf-8
#Filename:IfcWallStandardCase.py
import log
import common
from ifcwall import IFCWALL

from utils import *

class IFCWALLSTANDARDCASE(IFCWALL):
    """"""
    def __init__(self,id,arg):
        super(IFCWALLSTANDARDCASE,self).__init__(id,arg)
        self.type='IFCWALLSTANDARDCASE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCWALLSTANDARDCASE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWALLSTANDARDCASE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCWALLSTANDARDCASE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCWALLSTANDARDCASE,self).toString()       

        return line
