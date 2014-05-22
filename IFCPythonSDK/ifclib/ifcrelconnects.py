#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelConnects.py
import log
import common
from ifcrelationship import IFCRELATIONSHIP

from utils import *

class IFCRELCONNECTS(IFCRELATIONSHIP):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCONNECTS,self).__init__(id,arg)
        self.type='IFCRELCONNECTS'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCRELCONNECTS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCONNECTS,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCONNECTS,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCRELCONNECTS,self).toString()       

        return line
