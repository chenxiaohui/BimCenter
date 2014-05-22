#!/usr/bin/python
#coding=utf-8
#Filename:IfcWindow.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCWINDOW(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCWINDOW,self).__init__(id,arg)
        self.type='IFCWINDOW'
        self.inverse={}
        self.OverallHeight=None #IfcPositiveLengthMeasure
        self.OverallWidth=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCWINDOW,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWINDOW,self).init():
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
        return super(IFCWINDOW,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCWINDOW,self).toString()       
        line += integerToSPF(self.OverallHeight)+','
        line += integerToSPF(self.OverallWidth)+','

        return line
