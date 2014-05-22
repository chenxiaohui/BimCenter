#!/usr/bin/python
#coding=utf-8
#Filename:IfcCurtainWall.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCCURTAINWALL(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCCURTAINWALL,self).__init__(id,arg)
        self.type='IFCCURTAINWALL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCCURTAINWALL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCURTAINWALL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCURTAINWALL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCURTAINWALL,self).toString()       

        return line
