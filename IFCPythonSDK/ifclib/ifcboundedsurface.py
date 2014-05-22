#!/usr/bin/python
#coding=utf-8
#Filename:IfcBoundedSurface.py
import log
import common
from ifcsurface import IFCSURFACE

from utils import *

class IFCBOUNDEDSURFACE(IFCSURFACE):
    """"""
    def __init__(self,id,arg):
        super(IFCBOUNDEDSURFACE,self).__init__(id,arg)
        self.type='IFCBOUNDEDSURFACE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCBOUNDEDSURFACE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBOUNDEDSURFACE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBOUNDEDSURFACE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCBOUNDEDSURFACE,self).toString()       

        return line
