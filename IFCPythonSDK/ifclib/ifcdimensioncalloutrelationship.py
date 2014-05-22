#!/usr/bin/python
#coding=utf-8
#Filename:IfcDimensionCalloutRelationship.py
import log
import common
from ifcdraughtingcalloutrelationship import IFCDRAUGHTINGCALLOUTRELATIONSHIP

from utils import *

class IFCDIMENSIONCALLOUTRELATIONSHIP(IFCDRAUGHTINGCALLOUTRELATIONSHIP):
    """"""
    def __init__(self,id,arg):
        super(IFCDIMENSIONCALLOUTRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCDIMENSIONCALLOUTRELATIONSHIP'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDIMENSIONCALLOUTRELATIONSHIP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDIMENSIONCALLOUTRELATIONSHIP,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDIMENSIONCALLOUTRELATIONSHIP,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDIMENSIONCALLOUTRELATIONSHIP,self).toString()       

        return line
