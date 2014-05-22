#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertySet.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCPROPERTYSET(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYSET,self).__init__(id,arg)
        self.type='IFCPROPERTYSET'
        self.inverse={}
        self.HasProperties=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYSET,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYSET,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HasProperties= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYSET,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPROPERTYSET,self).toString()       
        line += listParamToSPF(self.HasProperties,idToSPF)+','

        return line
