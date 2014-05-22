#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurface.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCSURFACE(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCSURFACE,self).__init__(id,arg)
        self.type='IFCSURFACE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSURFACE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSURFACE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSURFACE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSURFACE,self).toString()       

        return line
