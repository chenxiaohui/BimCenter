#!/usr/bin/python
#coding=utf-8
#Filename:IfcTopologicalRepresentationItem.py
import log
import common
from ifcrepresentationitem import IFCREPRESENTATIONITEM

from utils import *

class IFCTOPOLOGICALREPRESENTATIONITEM(IFCREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCTOPOLOGICALREPRESENTATIONITEM,self).__init__(id,arg)
        self.type='IFCTOPOLOGICALREPRESENTATIONITEM'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCTOPOLOGICALREPRESENTATIONITEM,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTOPOLOGICALREPRESENTATIONITEM,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTOPOLOGICALREPRESENTATIONITEM,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCTOPOLOGICALREPRESENTATIONITEM,self).toString()       

        return line
