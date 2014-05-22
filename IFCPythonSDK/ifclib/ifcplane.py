#!/usr/bin/python
#coding=utf-8
#Filename:IfcPlane.py
import log
import common
from ifcelementarysurface import IFCELEMENTARYSURFACE

from utils import *

class IFCPLANE(IFCELEMENTARYSURFACE):
    """"""
    def __init__(self,id,arg):
        super(IFCPLANE,self).__init__(id,arg)
        self.type='IFCPLANE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPLANE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPLANE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPLANE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPLANE,self).toString()       

        return line
