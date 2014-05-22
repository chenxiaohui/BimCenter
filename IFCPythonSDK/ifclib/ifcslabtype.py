#!/usr/bin/python
#coding=utf-8
#Filename:IfcSlabType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCSLABTYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCSLABTYPE,self).__init__(id,arg)
        self.type='IFCSLABTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcSlabTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSLABTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSLABTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSLABTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSLABTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
