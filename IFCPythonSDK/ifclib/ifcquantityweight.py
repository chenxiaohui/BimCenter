#!/usr/bin/python
#coding=utf-8
#Filename:IfcQuantityWeight.py
import log
import common
from ifcphysicalsimplequantity import IFCPHYSICALSIMPLEQUANTITY

from utils import *

class IFCQUANTITYWEIGHT(IFCPHYSICALSIMPLEQUANTITY):
    """"""
    def __init__(self,id,arg):
        super(IFCQUANTITYWEIGHT,self).__init__(id,arg)
        self.type='IFCQUANTITYWEIGHT'
        self.inverse={}
        self.WeightValue=None #IfcMassMeasure


    def load(self):
        """register inverses"""
        if not super(IFCQUANTITYWEIGHT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCQUANTITYWEIGHT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WeightValue= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCQUANTITYWEIGHT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCQUANTITYWEIGHT,self).toString()       
        line += integerToSPF(self.WeightValue)+','

        return line