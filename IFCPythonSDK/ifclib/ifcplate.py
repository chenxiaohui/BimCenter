#!/usr/bin/python
#coding=utf-8
#Filename:IfcPlate.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCPLATE(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCPLATE,self).__init__(id,arg)
        self.type='IFCPLATE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPLATE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPLATE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPLATE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPLATE,self).toString()       

        return line
