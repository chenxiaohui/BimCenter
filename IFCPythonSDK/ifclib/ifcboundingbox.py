#!/usr/bin/python
#coding=utf-8
#Filename:IfcBoundingBox.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCBOUNDINGBOX(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCBOUNDINGBOX,self).__init__(id,arg)
        self.type='IFCBOUNDINGBOX'
        self.inverse={}
        self.Corner=None #IfcCartesianPoint
        self.XDim=None #IfcPositiveLengthMeasure
        self.YDim=None #IfcPositiveLengthMeasure
        self.ZDim=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCBOUNDINGBOX,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBOUNDINGBOX,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Corner= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.XDim= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.YDim= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ZDim= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBOUNDINGBOX,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCBOUNDINGBOX,self).toString()       
        line += idToSPF(self.Corner)+','
        line += integerToSPF(self.XDim)+','
        line += integerToSPF(self.YDim)+','
        line += integerToSPF(self.ZDim)+','

        return line
