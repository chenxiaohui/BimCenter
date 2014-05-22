#!/usr/bin/python
#coding=utf-8
#Filename:IfcPreDefinedPointMarkerSymbol.py
import log
import common
from ifcpredefinedsymbol import IFCPREDEFINEDSYMBOL

from utils import *

class IFCPREDEFINEDPOINTMARKERSYMBOL(IFCPREDEFINEDSYMBOL):
    """"""
    def __init__(self,id,arg):
        super(IFCPREDEFINEDPOINTMARKERSYMBOL,self).__init__(id,arg)
        self.type='IFCPREDEFINEDPOINTMARKERSYMBOL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPREDEFINEDPOINTMARKERSYMBOL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPREDEFINEDPOINTMARKERSYMBOL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPREDEFINEDPOINTMARKERSYMBOL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPREDEFINEDPOINTMARKERSYMBOL,self).toString()       

        return line
