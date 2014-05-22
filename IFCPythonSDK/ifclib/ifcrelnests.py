#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelNests.py
import log
import common
from ifcreldecomposes import IFCRELDECOMPOSES

from utils import *

class IFCRELNESTS(IFCRELDECOMPOSES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELNESTS,self).__init__(id,arg)
        self.type='IFCRELNESTS'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCRELNESTS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELNESTS,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELNESTS,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCRELNESTS,self).toString()       

        return line
