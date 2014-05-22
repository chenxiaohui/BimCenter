#!/usr/bin/python
#coding=utf-8
#Filename:IfcJunctionBoxType.py
import log
import common
from ifcflowfittingtype import IFCFLOWFITTINGTYPE

from utils import *

class IFCJUNCTIONBOXTYPE(IFCFLOWFITTINGTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCJUNCTIONBOXTYPE,self).__init__(id,arg)
        self.type='IFCJUNCTIONBOXTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcJunctionBoxTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCJUNCTIONBOXTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCJUNCTIONBOXTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCJUNCTIONBOXTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCJUNCTIONBOXTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
