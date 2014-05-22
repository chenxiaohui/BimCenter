#!/usr/bin/python
#coding=utf-8
#Filename:IfcAxis1Placement.py
import log
import common
from ifcplacement import IFCPLACEMENT

from utils import *

class IFCAXIS1PLACEMENT(IFCPLACEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCAXIS1PLACEMENT,self).__init__(id,arg)
        self.type='IFCAXIS1PLACEMENT'
        self.inverse={}
        self.Axis=None #IfcDirection


    def load(self):
        """register inverses"""
        if not super(IFCAXIS1PLACEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAXIS1PLACEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Axis= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAXIS1PLACEMENT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCAXIS1PLACEMENT,self).toString()       
        line += idToSPF(self.Axis)+','

        return line
