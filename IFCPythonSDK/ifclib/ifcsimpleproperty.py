#!/usr/bin/python
#coding=utf-8
#Filename:IfcSimpleProperty.py
import log
import common
from ifcproperty import IFCPROPERTY

from utils import *

class IFCSIMPLEPROPERTY(IFCPROPERTY):
    """"""
    def __init__(self,id,arg):
        super(IFCSIMPLEPROPERTY,self).__init__(id,arg)
        self.type='IFCSIMPLEPROPERTY'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSIMPLEPROPERTY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSIMPLEPROPERTY,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSIMPLEPROPERTY,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSIMPLEPROPERTY,self).toString()       

        return line
