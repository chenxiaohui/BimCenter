#!/usr/bin/python
#coding=utf-8
#Filename:IfcDraughtingPreDefinedColour.py
import log
import common
from ifcpredefinedcolour import IFCPREDEFINEDCOLOUR

from utils import *

class IFCDRAUGHTINGPREDEFINEDCOLOUR(IFCPREDEFINEDCOLOUR):
    """"""
    def __init__(self,id,arg):
        super(IFCDRAUGHTINGPREDEFINEDCOLOUR,self).__init__(id,arg)
        self.type='IFCDRAUGHTINGPREDEFINEDCOLOUR'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDRAUGHTINGPREDEFINEDCOLOUR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDRAUGHTINGPREDEFINEDCOLOUR,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDRAUGHTINGPREDEFINEDCOLOUR,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDRAUGHTINGPREDEFINEDCOLOUR,self).toString()       

        return line
