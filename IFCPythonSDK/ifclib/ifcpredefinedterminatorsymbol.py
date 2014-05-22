#!/usr/bin/python
#coding=utf-8
#Filename:IfcPreDefinedTerminatorSymbol.py
import log
import common
from ifcpredefinedsymbol import IFCPREDEFINEDSYMBOL

from utils import *

class IFCPREDEFINEDTERMINATORSYMBOL(IFCPREDEFINEDSYMBOL):
    """"""
    def __init__(self,id,arg):
        super(IFCPREDEFINEDTERMINATORSYMBOL,self).__init__(id,arg)
        self.type='IFCPREDEFINEDTERMINATORSYMBOL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPREDEFINEDTERMINATORSYMBOL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPREDEFINEDTERMINATORSYMBOL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPREDEFINEDTERMINATORSYMBOL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPREDEFINEDTERMINATORSYMBOL,self).toString()       

        return line
