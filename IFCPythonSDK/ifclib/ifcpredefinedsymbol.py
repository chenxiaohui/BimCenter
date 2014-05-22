#!/usr/bin/python
#coding=utf-8
#Filename:IfcPreDefinedSymbol.py
import log
import common
from ifcpredefineditem import IFCPREDEFINEDITEM

from utils import *

class IFCPREDEFINEDSYMBOL(IFCPREDEFINEDITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCPREDEFINEDSYMBOL,self).__init__(id,arg)
        self.type='IFCPREDEFINEDSYMBOL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPREDEFINEDSYMBOL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPREDEFINEDSYMBOL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPREDEFINEDSYMBOL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPREDEFINEDSYMBOL,self).toString()       

        return line
