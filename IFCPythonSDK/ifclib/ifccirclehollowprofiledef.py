#!/usr/bin/python
#coding=utf-8
#Filename:IfcCircleHollowProfileDef.py
import log
import common
from ifccircleprofiledef import IFCCIRCLEPROFILEDEF

from utils import *

class IFCCIRCLEHOLLOWPROFILEDEF(IFCCIRCLEPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCCIRCLEHOLLOWPROFILEDEF,self).__init__(id,arg)
        self.type='IFCCIRCLEHOLLOWPROFILEDEF'
        self.inverse={}
        self.WallThickness=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCIRCLEHOLLOWPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCIRCLEHOLLOWPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WallThickness= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCIRCLEHOLLOWPROFILEDEF,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCIRCLEHOLLOWPROFILEDEF,self).toString()       
        line += integerToSPF(self.WallThickness)+','

        return line
