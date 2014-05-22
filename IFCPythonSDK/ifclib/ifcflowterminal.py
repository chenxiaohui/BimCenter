#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowTerminal.py
import log
import common
from ifcdistributionflowelement import IFCDISTRIBUTIONFLOWELEMENT

from utils import *

class IFCFLOWTERMINAL(IFCDISTRIBUTIONFLOWELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWTERMINAL,self).__init__(id,arg)
        self.type='IFCFLOWTERMINAL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWTERMINAL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWTERMINAL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWTERMINAL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWTERMINAL,self).toString()       

        return line
