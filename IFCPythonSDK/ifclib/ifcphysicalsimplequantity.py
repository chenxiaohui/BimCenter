#!/usr/bin/python
#coding=utf-8
#Filename:IfcPhysicalSimpleQuantity.py
import log
import common
from ifcphysicalquantity import IFCPHYSICALQUANTITY

from utils import *

class IFCPHYSICALSIMPLEQUANTITY(IFCPHYSICALQUANTITY):
    """"""
    def __init__(self,id,arg):
        super(IFCPHYSICALSIMPLEQUANTITY,self).__init__(id,arg)
        self.type='IFCPHYSICALSIMPLEQUANTITY'
        self.inverse={}
        self.Unit=None #IfcNamedUnit


    def load(self):
        """register inverses"""
        if not super(IFCPHYSICALSIMPLEQUANTITY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPHYSICALSIMPLEQUANTITY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Unit= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPHYSICALSIMPLEQUANTITY,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPHYSICALSIMPLEQUANTITY,self).toString()       
        line += idToSPF(self.Unit)+','

        return line
