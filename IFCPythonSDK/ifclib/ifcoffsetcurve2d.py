#!/usr/bin/python
#coding=utf-8
#Filename:IfcOffsetCurve2D.py
import log
import common
from ifccurve import IFCCURVE

from utils import *

class IFCOFFSETCURVE2D(IFCCURVE):
    """"""
    def __init__(self,id,arg):
        super(IFCOFFSETCURVE2D,self).__init__(id,arg)
        self.type='IFCOFFSETCURVE2D'
        self.inverse={}
        self.BasisCurve=None #IfcCurve
        self.Distance=None #IfcLengthMeasure
        self.SelfIntersect=None #LOGICAL


    def load(self):
        """register inverses"""
        if not super(IFCOFFSETCURVE2D,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCOFFSETCURVE2D,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BasisCurve= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Distance= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SelfIntersect= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCOFFSETCURVE2D,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCOFFSETCURVE2D,self).toString()       
        line += idToSPF(self.BasisCurve)+','
        line += integerToSPF(self.Distance)+','
        line += logicalToSPF(self.SelfIntersect)+','

        return line
