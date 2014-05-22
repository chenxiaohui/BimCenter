#!/usr/bin/python
#coding=utf-8
#Filename:IfcQuantityArea.py
import log
import common
from ifcphysicalsimplequantity import IFCPHYSICALSIMPLEQUANTITY

from utils import *

class IFCQUANTITYAREA(IFCPHYSICALSIMPLEQUANTITY):
    """"""
    def __init__(self,id,arg):
        super(IFCQUANTITYAREA,self).__init__(id,arg)
        self.type='IFCQUANTITYAREA'
        self.inverse={}
        self.AreaValue=None #IfcAreaMeasure


    def load(self):
        """register inverses"""
        if not super(IFCQUANTITYAREA,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCQUANTITYAREA,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AreaValue= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCQUANTITYAREA,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCQUANTITYAREA,self).toString()       
        line += integerToSPF(self.AreaValue)+','

        return line
