#!/usr/bin/python
#coding=utf-8
#Filename:IfcCostItem.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCCOSTITEM(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCCOSTITEM,self).__init__(id,arg)
        self.type='IFCCOSTITEM'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCCOSTITEM,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOSTITEM,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOSTITEM,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCOSTITEM,self).toString()       

        return line
