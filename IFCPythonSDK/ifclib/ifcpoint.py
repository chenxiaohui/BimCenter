#!/usr/bin/python
#coding=utf-8
#Filename:IfcPoint.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCPOINT(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCPOINT,self).__init__(id,arg)
        self.type='IFCPOINT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPOINT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPOINT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPOINT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPOINT,self).toString()       

        return line
