#!/usr/bin/python
#coding=utf-8
#Filename:IfcConic.py
import log
import common
from ifccurve import IFCCURVE

from utils import *

class IFCCONIC(IFCCURVE):
    """"""
    def __init__(self,id,arg):
        super(IFCCONIC,self).__init__(id,arg)
        self.type='IFCCONIC'
        self.inverse={}
        self.Position=None #IfcAxis2Placement


    def load(self):
        """register inverses"""
        if not super(IFCCONIC,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONIC,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Position= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONIC,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCONIC,self).toString()       
        line += typerefToSPF(self.Position)+','

        return line
