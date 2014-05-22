#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelOverridesProperties.py
import log
import common
from ifcreldefinesbyproperties import IFCRELDEFINESBYPROPERTIES

from utils import *

class IFCRELOVERRIDESPROPERTIES(IFCRELDEFINESBYPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELOVERRIDESPROPERTIES,self).__init__(id,arg)
        self.type='IFCRELOVERRIDESPROPERTIES'
        self.inverse={}
        self.OverridingProperties=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCRELOVERRIDESPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELOVERRIDESPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OverridingProperties= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELOVERRIDESPROPERTIES,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELOVERRIDESPROPERTIES,self).toString()       
        line += listParamToSPF(self.OverridingProperties,idToSPF)+','

        return line
