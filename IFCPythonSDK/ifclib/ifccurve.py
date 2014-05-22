#!/usr/bin/python
#coding=utf-8
#Filename:IfcCurve.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCCURVE(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCCURVE,self).__init__(id,arg)
        self.type='IFCCURVE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCCURVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCURVE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCURVE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCURVE,self).toString()       

        return line
