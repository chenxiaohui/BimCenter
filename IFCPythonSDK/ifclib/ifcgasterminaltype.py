#!/usr/bin/python
#coding=utf-8
#Filename:IfcGasTerminalType.py
import log
import common
from ifcflowterminaltype import IFCFLOWTERMINALTYPE

from utils import *

class IFCGASTERMINALTYPE(IFCFLOWTERMINALTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCGASTERMINALTYPE,self).__init__(id,arg)
        self.type='IFCGASTERMINALTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcGasTerminalTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCGASTERMINALTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGASTERMINALTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGASTERMINALTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCGASTERMINALTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
