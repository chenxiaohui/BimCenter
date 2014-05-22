#!/usr/bin/python
#coding=utf-8
#Filename:IfcPhysicalQuantity.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPHYSICALQUANTITY(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPHYSICALQUANTITY,self).__init__(id,arg)
        self.type='IFCPHYSICALQUANTITY'
        self.inverse={}
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.inverse['PartOfComplex']=[] #inverse:SET of IfcPhysicalComplexQuantity


    def load(self):
        """register inverses"""
        if not super(IFCPHYSICALQUANTITY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPHYSICALQUANTITY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        inverses = self.args.getInverses('IFCPHYSICALCOMPLEXQUANTITY', 'HasQuantities');
        if inverses:
            self.inverse['PartOfComplex']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPHYSICALQUANTITY,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPHYSICALQUANTITY,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','

        return line
