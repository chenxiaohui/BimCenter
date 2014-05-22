#!/usr/bin/python
#coding=utf-8
#Filename:IfcDoor.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCDOOR(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCDOOR,self).__init__(id,arg)
        self.type='IFCDOOR'
        self.inverse={}
        self.OverallHeight=None #IfcPositiveLengthMeasure
        self.OverallWidth=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCDOOR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDOOR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OverallHeight= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OverallWidth= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDOOR,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCDOOR,self).toString()       
        line += integerToSPF(self.OverallHeight)+','
        line += integerToSPF(self.OverallWidth)+','

        return line
