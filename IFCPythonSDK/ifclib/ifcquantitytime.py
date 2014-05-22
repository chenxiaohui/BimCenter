#!/usr/bin/python
#coding=utf-8
#Filename:IfcQuantityTime.py
import log
import common
from ifcphysicalsimplequantity import IFCPHYSICALSIMPLEQUANTITY

from utils import *

class IFCQUANTITYTIME(IFCPHYSICALSIMPLEQUANTITY):
    """"""
    def __init__(self,id,arg):
        super(IFCQUANTITYTIME,self).__init__(id,arg)
        self.type='IFCQUANTITYTIME'
        self.inverse={}
        self.TimeValue=None #IfcTimeMeasure


    def load(self):
        """register inverses"""
        if not super(IFCQUANTITYTIME,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCQUANTITYTIME,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TimeValue= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCQUANTITYTIME,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCQUANTITYTIME,self).toString()       
        line += integerToSPF(self.TimeValue)+','

        return line
