#!/usr/bin/python
#coding=utf-8
#Filename:IfcRectangleHollowProfileDef.py
import log
import common
from ifcrectangleprofiledef import IFCRECTANGLEPROFILEDEF

from utils import *

class IFCRECTANGLEHOLLOWPROFILEDEF(IFCRECTANGLEPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCRECTANGLEHOLLOWPROFILEDEF,self).__init__(id,arg)
        self.type='IFCRECTANGLEHOLLOWPROFILEDEF'
        self.inverse={}
        self.WallThickness=None #IfcPositiveLengthMeasure
        self.InnerFilletRadius=None #IfcPositiveLengthMeasure
        self.OuterFilletRadius=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCRECTANGLEHOLLOWPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRECTANGLEHOLLOWPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WallThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InnerFilletRadius= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OuterFilletRadius= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRECTANGLEHOLLOWPROFILEDEF,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCRECTANGLEHOLLOWPROFILEDEF,self).toString()       
        line += integerToSPF(self.WallThickness)+','
        line += integerToSPF(self.InnerFilletRadius)+','
        line += integerToSPF(self.OuterFilletRadius)+','

        return line
