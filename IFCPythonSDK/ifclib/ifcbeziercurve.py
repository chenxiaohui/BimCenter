#!/usr/bin/python
#coding=utf-8
#Filename:IfcBezierCurve.py
import log
import common
from ifcbsplinecurve import IFCBSPLINECURVE

from utils import *

class IFCBEZIERCURVE(IFCBSPLINECURVE):
    """"""
    def __init__(self,id,arg):
        super(IFCBEZIERCURVE,self).__init__(id,arg)
        self.type='IFCBEZIERCURVE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCBEZIERCURVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBEZIERCURVE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBEZIERCURVE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCBEZIERCURVE,self).toString()       

        return line
