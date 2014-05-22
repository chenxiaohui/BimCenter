#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralPointAction.py
import log
import common
from ifcstructuralaction import IFCSTRUCTURALACTION

from utils import *

class IFCSTRUCTURALPOINTACTION(IFCSTRUCTURALACTION):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALPOINTACTION,self).__init__(id,arg)
        self.type='IFCSTRUCTURALPOINTACTION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALPOINTACTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALPOINTACTION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALPOINTACTION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALPOINTACTION,self).toString()       

        return line
