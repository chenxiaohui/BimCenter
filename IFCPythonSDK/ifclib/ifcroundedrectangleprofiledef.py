#!/usr/bin/python
#coding=utf-8
#Filename:IfcRoundedRectangleProfileDef.py
import log
import common
from ifcrectangleprofiledef import IFCRECTANGLEPROFILEDEF

from utils import *

class IFCROUNDEDRECTANGLEPROFILEDEF(IFCRECTANGLEPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCROUNDEDRECTANGLEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCROUNDEDRECTANGLEPROFILEDEF'
        self.inverse={}
        self.RoundingRadius=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCROUNDEDRECTANGLEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCROUNDEDRECTANGLEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RoundingRadius= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCROUNDEDRECTANGLEPROFILEDEF,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCROUNDEDRECTANGLEPROFILEDEF,self).toString()       
        line += integerToSPF(self.RoundingRadius)+','

        return line
