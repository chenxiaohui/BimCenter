#!/usr/bin/python
#coding=utf-8
#Filename:IfcCurveStyle.py
import log
import common
from ifcpresentationstyle import IFCPRESENTATIONSTYLE

from utils import *

class IFCCURVESTYLE(IFCPRESENTATIONSTYLE):
    """"""
    def __init__(self,id,arg):
        super(IFCCURVESTYLE,self).__init__(id,arg)
        self.type='IFCCURVESTYLE'
        self.inverse={}
        self.CurveFont=None #IfcCurveFontOrScaledCurveFontSelect
        self.CurveWidth=None #IfcSizeSelect
        self.CurveColour=None #IfcColour


    def load(self):
        """register inverses"""
        if not super(IFCCURVESTYLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCURVESTYLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CurveFont= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CurveWidth= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CurveColour= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCURVESTYLE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCCURVESTYLE,self).toString()       
        line += typerefToSPF(self.CurveFont)+','
        line += typerefToSPF(self.CurveWidth)+','
        line += typerefToSPF(self.CurveColour)+','

        return line
