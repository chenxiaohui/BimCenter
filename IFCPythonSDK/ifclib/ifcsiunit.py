#!/usr/bin/python
#coding=utf-8
#Filename:IfcSIUnit.py
import log
import common
from ifcnamedunit import IFCNAMEDUNIT

from utils import *

class IFCSIUNIT(IFCNAMEDUNIT):
    """"""
    def __init__(self,id,arg):
        super(IFCSIUNIT,self).__init__(id,arg)
        self.type='IFCSIUNIT'
        self.inverse={}
        self.Prefix=None #IfcSIPrefix
        self.Name=None #IfcSIUnitName


    def load(self):
        """register inverses"""
        if not super(IFCSIUNIT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSIUNIT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Prefix= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSIUNIT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSIUNIT,self).toString()       
        line += typerefToSPF(self.Prefix)+','
        line += typerefToSPF(self.Name)+','

        return line
