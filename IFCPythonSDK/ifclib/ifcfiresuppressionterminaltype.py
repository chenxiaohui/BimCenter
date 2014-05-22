#!/usr/bin/python
#coding=utf-8
#Filename:IfcFireSuppressionTerminalType.py
import log
import common
from ifcflowterminaltype import IFCFLOWTERMINALTYPE

from utils import *

class IFCFIRESUPPRESSIONTERMINALTYPE(IFCFLOWTERMINALTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFIRESUPPRESSIONTERMINALTYPE,self).__init__(id,arg)
        self.type='IFCFIRESUPPRESSIONTERMINALTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcFireSuppressionTerminalTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCFIRESUPPRESSIONTERMINALTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFIRESUPPRESSIONTERMINALTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFIRESUPPRESSIONTERMINALTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFIRESUPPRESSIONTERMINALTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
