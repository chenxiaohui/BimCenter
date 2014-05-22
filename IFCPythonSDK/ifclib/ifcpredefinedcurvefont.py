#!/usr/bin/python
#coding=utf-8
#Filename:IfcPreDefinedCurveFont.py
import log
import common
from ifcpredefineditem import IFCPREDEFINEDITEM

from utils import *

class IFCPREDEFINEDCURVEFONT(IFCPREDEFINEDITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCPREDEFINEDCURVEFONT,self).__init__(id,arg)
        self.type='IFCPREDEFINEDCURVEFONT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPREDEFINEDCURVEFONT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPREDEFINEDCURVEFONT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPREDEFINEDCURVEFONT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPREDEFINEDCURVEFONT,self).toString()       

        return line
