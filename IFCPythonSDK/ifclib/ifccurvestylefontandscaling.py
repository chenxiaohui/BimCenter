#!/usr/bin/python
#coding=utf-8
#Filename:IfcCurveStyleFontAndScaling.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCURVESTYLEFONTANDSCALING(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCURVESTYLEFONTANDSCALING,self).__init__(id,arg)
        self.type='IFCCURVESTYLEFONTANDSCALING'
        self.inverse={}
        self.Name=None #IfcLabel
        self.CurveFont=None #IfcCurveStyleFontSelect
        self.CurveFontScaling=None #IfcPositiveRatioMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCURVESTYLEFONTANDSCALING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCURVESTYLEFONTANDSCALING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CurveFont= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CurveFontScaling= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCURVESTYLEFONTANDSCALING,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCCURVESTYLEFONTANDSCALING,self).toString()       
        line += strToSPF(self.Name)+','
        line += typerefToSPF(self.CurveFont)+','
        line += integerToSPF(self.CurveFontScaling)+','

        return line
