#!/usr/bin/python
#coding=utf-8
#Filename:IfcDerivedUnitElement.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCDERIVEDUNITELEMENT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCDERIVEDUNITELEMENT,self).__init__(id,arg)
        self.type='IFCDERIVEDUNITELEMENT'
        self.inverse={}
        self.Unit=None #IfcNamedUnit
        self.Exponent=None #INTEGER


    def load(self):
        """register inverses"""
        if not super(IFCDERIVEDUNITELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDERIVEDUNITELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Unit= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Exponent= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDERIVEDUNITELEMENT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCDERIVEDUNITELEMENT,self).toString()       
        line += idToSPF(self.Unit)+','
        line += integerToSPF(self.Exponent)+','

        return line
