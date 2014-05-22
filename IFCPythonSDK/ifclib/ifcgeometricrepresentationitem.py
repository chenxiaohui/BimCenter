#!/usr/bin/python
#coding=utf-8
#Filename:IfcGeometricRepresentationItem.py
import log
import common
from ifcrepresentationitem import IFCREPRESENTATIONITEM

from utils import *

class IFCGEOMETRICREPRESENTATIONITEM(IFCREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCGEOMETRICREPRESENTATIONITEM,self).__init__(id,arg)
        self.type='IFCGEOMETRICREPRESENTATIONITEM'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCGEOMETRICREPRESENTATIONITEM,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGEOMETRICREPRESENTATIONITEM,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGEOMETRICREPRESENTATIONITEM,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCGEOMETRICREPRESENTATIONITEM,self).toString()       

        return line
