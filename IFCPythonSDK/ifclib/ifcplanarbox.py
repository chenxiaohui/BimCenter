#!/usr/bin/python
#coding=utf-8
#Filename:IfcPlanarBox.py
import log
import common
from ifcplanarextent import IFCPLANAREXTENT

from utils import *

class IFCPLANARBOX(IFCPLANAREXTENT):
    """"""
    def __init__(self,id,arg):
        super(IFCPLANARBOX,self).__init__(id,arg)
        self.type='IFCPLANARBOX'
        self.inverse={}
        self.Placement=None #IfcAxis2Placement


    def load(self):
        """register inverses"""
        if not super(IFCPLANARBOX,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPLANARBOX,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Placement= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPLANARBOX,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPLANARBOX,self).toString()       
        line += typerefToSPF(self.Placement)+','

        return line
