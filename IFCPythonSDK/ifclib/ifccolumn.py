#!/usr/bin/python
#coding=utf-8
#Filename:IfcColumn.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCCOLUMN(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCCOLUMN,self).__init__(id,arg)
        self.type='IFCCOLUMN'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCCOLUMN,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOLUMN,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOLUMN,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCOLUMN,self).toString()       

        return line
