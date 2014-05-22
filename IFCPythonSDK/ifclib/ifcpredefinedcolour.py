#!/usr/bin/python
#coding=utf-8
#Filename:IfcPreDefinedColour.py
import log
import common
from ifcpredefineditem import IFCPREDEFINEDITEM

from utils import *

class IFCPREDEFINEDCOLOUR(IFCPREDEFINEDITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCPREDEFINEDCOLOUR,self).__init__(id,arg)
        self.type='IFCPREDEFINEDCOLOUR'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPREDEFINEDCOLOUR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPREDEFINEDCOLOUR,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPREDEFINEDCOLOUR,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPREDEFINEDCOLOUR,self).toString()       

        return line
