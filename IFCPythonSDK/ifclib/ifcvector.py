#!/usr/bin/python
#coding=utf-8
#Filename:IfcVector.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCVECTOR(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCVECTOR,self).__init__(id,arg)
        self.type='IFCVECTOR'
        self.inverse={}
        self.Orientation=None #IfcDirection
        self.Magnitude=None #IfcLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCVECTOR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCVECTOR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Orientation= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Magnitude= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCVECTOR,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCVECTOR,self).toString()       
        line += idToSPF(self.Orientation)+','
        line += integerToSPF(self.Magnitude)+','

        return line
