#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAggregates.py
import log
import common
from ifcreldecomposes import IFCRELDECOMPOSES

from utils import *

class IFCRELAGGREGATES(IFCRELDECOMPOSES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELAGGREGATES,self).__init__(id,arg)
        self.type='IFCRELAGGREGATES'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCRELAGGREGATES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELAGGREGATES,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELAGGREGATES,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCRELAGGREGATES,self).toString()       

        return line
