#!/usr/bin/python
#coding=utf-8
#Filename:IfcUnitAssignment.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCUNITASSIGNMENT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCUNITASSIGNMENT,self).__init__(id,arg)
        self.type='IFCUNITASSIGNMENT'
        self.inverse={}
        self.Units=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCUNITASSIGNMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCUNITASSIGNMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Units= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCUNITASSIGNMENT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCUNITASSIGNMENT,self).toString()       
        line += listParamToSPF(self.Units,typerefToSPF)+','

        return line
