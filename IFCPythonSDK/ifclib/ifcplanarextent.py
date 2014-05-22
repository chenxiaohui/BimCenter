#!/usr/bin/python
#coding=utf-8
#Filename:IfcPlanarExtent.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCPLANAREXTENT(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCPLANAREXTENT,self).__init__(id,arg)
        self.type='IFCPLANAREXTENT'
        self.inverse={}
        self.SizeInX=None #IfcLengthMeasure
        self.SizeInY=None #IfcLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCPLANAREXTENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPLANAREXTENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SizeInX= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SizeInY= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPLANAREXTENT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPLANAREXTENT,self).toString()       
        line += integerToSPF(self.SizeInX)+','
        line += integerToSPF(self.SizeInY)+','

        return line
