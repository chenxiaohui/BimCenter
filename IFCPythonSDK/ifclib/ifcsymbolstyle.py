#!/usr/bin/python
#coding=utf-8
#Filename:IfcSymbolStyle.py
import log
import common
from ifcpresentationstyle import IFCPRESENTATIONSTYLE

from utils import *

class IFCSYMBOLSTYLE(IFCPRESENTATIONSTYLE):
    """"""
    def __init__(self,id,arg):
        super(IFCSYMBOLSTYLE,self).__init__(id,arg)
        self.type='IFCSYMBOLSTYLE'
        self.inverse={}
        self.StyleOfSymbol=None #IfcSymbolStyleSelect


    def load(self):
        """register inverses"""
        if not super(IFCSYMBOLSTYLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSYMBOLSTYLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.StyleOfSymbol= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSYMBOLSTYLE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSYMBOLSTYLE,self).toString()       
        line += typerefToSPF(self.StyleOfSymbol)+','

        return line
