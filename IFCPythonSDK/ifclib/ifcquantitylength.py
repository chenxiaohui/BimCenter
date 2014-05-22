#!/usr/bin/python
#coding=utf-8
#Filename:IfcQuantityLength.py
import log
import common
from ifcphysicalsimplequantity import IFCPHYSICALSIMPLEQUANTITY

from utils import *

class IFCQUANTITYLENGTH(IFCPHYSICALSIMPLEQUANTITY):
    """"""
    def __init__(self,id,arg):
        super(IFCQUANTITYLENGTH,self).__init__(id,arg)
        self.type='IFCQUANTITYLENGTH'
        self.inverse={}
        self.LengthValue=None #IfcLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCQUANTITYLENGTH,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCQUANTITYLENGTH,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LengthValue= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCQUANTITYLENGTH,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCQUANTITYLENGTH,self).toString()       
        line += integerToSPF(self.LengthValue)+','

        return line
