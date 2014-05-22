#!/usr/bin/python
#coding=utf-8
#Filename:IfcAirTerminalType.py
import log
import common
from ifcflowterminaltype import IFCFLOWTERMINALTYPE

from utils import *

class IFCAIRTERMINALTYPE(IFCFLOWTERMINALTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCAIRTERMINALTYPE,self).__init__(id,arg)
        self.type='IFCAIRTERMINALTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcAirTerminalTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCAIRTERMINALTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAIRTERMINALTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAIRTERMINALTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCAIRTERMINALTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
