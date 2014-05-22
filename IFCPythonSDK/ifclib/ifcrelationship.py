#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelationship.py
import log
import common
from ifcroot import IFCROOT

from utils import *

class IFCRELATIONSHIP(IFCROOT):
    """"""
    def __init__(self,id,arg):
        super(IFCRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCRELATIONSHIP'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCRELATIONSHIP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELATIONSHIP,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELATIONSHIP,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCRELATIONSHIP,self).toString()       

        return line
