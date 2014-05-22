#!/usr/bin/python
#coding=utf-8
#Filename:IfcBoundedCurve.py
import log
import common
from ifccurve import IFCCURVE

from utils import *

class IFCBOUNDEDCURVE(IFCCURVE):
    """"""
    def __init__(self,id,arg):
        super(IFCBOUNDEDCURVE,self).__init__(id,arg)
        self.type='IFCBOUNDEDCURVE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCBOUNDEDCURVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBOUNDEDCURVE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBOUNDEDCURVE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCBOUNDEDCURVE,self).toString()       

        return line
