#!/usr/bin/python
#coding=utf-8
#Filename:IfcSystemFurnitureElementType.py
import log
import common
from ifcfurnishingelementtype import IFCFURNISHINGELEMENTTYPE

from utils import *

class IFCSYSTEMFURNITUREELEMENTTYPE(IFCFURNISHINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCSYSTEMFURNITUREELEMENTTYPE,self).__init__(id,arg)
        self.type='IFCSYSTEMFURNITUREELEMENTTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSYSTEMFURNITUREELEMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSYSTEMFURNITUREELEMENTTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSYSTEMFURNITUREELEMENTTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSYSTEMFURNITUREELEMENTTYPE,self).toString()       

        return line
