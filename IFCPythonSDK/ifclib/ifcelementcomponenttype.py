#!/usr/bin/python
#coding=utf-8
#Filename:IfcElementComponentType.py
import log
import common
from ifcelementtype import IFCELEMENTTYPE

from utils import *

class IFCELEMENTCOMPONENTTYPE(IFCELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCELEMENTCOMPONENTTYPE,self).__init__(id,arg)
        self.type='IFCELEMENTCOMPONENTTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCELEMENTCOMPONENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELEMENTCOMPONENTTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELEMENTCOMPONENTTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCELEMENTCOMPONENTTYPE,self).toString()       

        return line
