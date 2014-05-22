#!/usr/bin/python
#coding=utf-8
#Filename:IfcCurveStyleFontPattern.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCURVESTYLEFONTPATTERN(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCURVESTYLEFONTPATTERN,self).__init__(id,arg)
        self.type='IFCCURVESTYLEFONTPATTERN'
        self.inverse={}
        self.VisibleSegmentLength=None #IfcLengthMeasure
        self.InvisibleSegmentLength=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCURVESTYLEFONTPATTERN,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCURVESTYLEFONTPATTERN,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VisibleSegmentLength= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InvisibleSegmentLength= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCURVESTYLEFONTPATTERN,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCURVESTYLEFONTPATTERN,self).toString()       
        line += integerToSPF(self.VisibleSegmentLength)+','
        line += integerToSPF(self.InvisibleSegmentLength)+','

        return line
