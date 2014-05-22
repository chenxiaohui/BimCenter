#!/usr/bin/python
#coding=utf-8
#Filename:IfcCircle.py
import log
import common
from ifcconic import IFCCONIC

from utils import *

class IFCCIRCLE(IFCCONIC):
    """"""
    def __init__(self,id,arg):
        super(IFCCIRCLE,self).__init__(id,arg)
        self.type='IFCCIRCLE'
        self.inverse={}
        self.Radius=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCIRCLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCIRCLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Radius= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCIRCLE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCIRCLE,self).toString()       
        line += integerToSPF(self.Radius)+','

        return line
