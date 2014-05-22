#!/usr/bin/python
#coding=utf-8
#Filename:IfcLoop.py
import log
import common
from ifctopologicalrepresentationitem import IFCTOPOLOGICALREPRESENTATIONITEM

from utils import *

class IFCLOOP(IFCTOPOLOGICALREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCLOOP,self).__init__(id,arg)
        self.type='IFCLOOP'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCLOOP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLOOP,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLOOP,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCLOOP,self).toString()       

        return line
