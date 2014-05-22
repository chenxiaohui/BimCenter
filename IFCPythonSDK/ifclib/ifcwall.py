#!/usr/bin/python
#coding=utf-8
#Filename:IfcWall.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCWALL(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCWALL,self).__init__(id,arg)
        self.type='IFCWALL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCWALL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWALL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCWALL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCWALL,self).toString()       

        return line
