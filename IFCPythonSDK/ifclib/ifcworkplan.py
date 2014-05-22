#!/usr/bin/python
#coding=utf-8
#Filename:IfcWorkPlan.py
import log
import common
from ifcworkcontrol import IFCWORKCONTROL

from utils import *

class IFCWORKPLAN(IFCWORKCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCWORKPLAN,self).__init__(id,arg)
        self.type='IFCWORKPLAN'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCWORKPLAN,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWORKPLAN,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCWORKPLAN,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCWORKPLAN,self).toString()       

        return line
