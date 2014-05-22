#!/usr/bin/python
#coding=utf-8
#Filename:IfcDraughtingPreDefinedCurveFont.py
import log
import common
from ifcpredefinedcurvefont import IFCPREDEFINEDCURVEFONT

from utils import *

class IFCDRAUGHTINGPREDEFINEDCURVEFONT(IFCPREDEFINEDCURVEFONT):
    """"""
    def __init__(self,id,arg):
        super(IFCDRAUGHTINGPREDEFINEDCURVEFONT,self).__init__(id,arg)
        self.type='IFCDRAUGHTINGPREDEFINEDCURVEFONT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDRAUGHTINGPREDEFINEDCURVEFONT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDRAUGHTINGPREDEFINEDCURVEFONT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDRAUGHTINGPREDEFINEDCURVEFONT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDRAUGHTINGPREDEFINEDCURVEFONT,self).toString()       

        return line
