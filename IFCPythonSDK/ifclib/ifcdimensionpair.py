#!/usr/bin/python
#coding=utf-8
#Filename:IfcDimensionPair.py
import log
import common
from ifcdraughtingcalloutrelationship import IFCDRAUGHTINGCALLOUTRELATIONSHIP

from utils import *

class IFCDIMENSIONPAIR(IFCDRAUGHTINGCALLOUTRELATIONSHIP):
    """"""
    def __init__(self,id,arg):
        super(IFCDIMENSIONPAIR,self).__init__(id,arg)
        self.type='IFCDIMENSIONPAIR'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDIMENSIONPAIR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDIMENSIONPAIR,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDIMENSIONPAIR,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDIMENSIONPAIR,self).toString()       

        return line
