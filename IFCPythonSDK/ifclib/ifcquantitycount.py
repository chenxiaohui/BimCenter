#!/usr/bin/python
#coding=utf-8
#Filename:IfcQuantityCount.py
import log
import common
from ifcphysicalsimplequantity import IFCPHYSICALSIMPLEQUANTITY

from utils import *

class IFCQUANTITYCOUNT(IFCPHYSICALSIMPLEQUANTITY):
    """"""
    def __init__(self,id,arg):
        super(IFCQUANTITYCOUNT,self).__init__(id,arg)
        self.type='IFCQUANTITYCOUNT'
        self.inverse={}
        self.CountValue=None #IfcCountMeasure


    def load(self):
        """register inverses"""
        if not super(IFCQUANTITYCOUNT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCQUANTITYCOUNT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CountValue= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCQUANTITYCOUNT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCQUANTITYCOUNT,self).toString()       
        line += integerToSPF(self.CountValue)+','

        return line
