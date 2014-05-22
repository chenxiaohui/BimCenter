#!/usr/bin/python
#coding=utf-8
#Filename:IfcPreDefinedDimensionSymbol.py
import log
import common
from ifcpredefinedsymbol import IFCPREDEFINEDSYMBOL

from utils import *

class IFCPREDEFINEDDIMENSIONSYMBOL(IFCPREDEFINEDSYMBOL):
    """"""
    def __init__(self,id,arg):
        super(IFCPREDEFINEDDIMENSIONSYMBOL,self).__init__(id,arg)
        self.type='IFCPREDEFINEDDIMENSIONSYMBOL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPREDEFINEDDIMENSIONSYMBOL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPREDEFINEDDIMENSIONSYMBOL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPREDEFINEDDIMENSIONSYMBOL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPREDEFINEDDIMENSIONSYMBOL,self).toString()       

        return line
