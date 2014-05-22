#!/usr/bin/python
#coding=utf-8
#Filename:IfcFurnishingElementType.py
import log
import common
from ifcelementtype import IFCELEMENTTYPE

from utils import *

class IFCFURNISHINGELEMENTTYPE(IFCELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFURNISHINGELEMENTTYPE,self).__init__(id,arg)
        self.type='IFCFURNISHINGELEMENTTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFURNISHINGELEMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFURNISHINGELEMENTTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFURNISHINGELEMENTTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFURNISHINGELEMENTTYPE,self).toString()       

        return line
