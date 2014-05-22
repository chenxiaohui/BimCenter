#!/usr/bin/python
#coding=utf-8
#Filename:IfcStyledRepresentation.py
import log
import common
from ifcstylemodel import IFCSTYLEMODEL

from utils import *

class IFCSTYLEDREPRESENTATION(IFCSTYLEMODEL):
    """"""
    def __init__(self,id,arg):
        super(IFCSTYLEDREPRESENTATION,self).__init__(id,arg)
        self.type='IFCSTYLEDREPRESENTATION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSTYLEDREPRESENTATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTYLEDREPRESENTATION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTYLEDREPRESENTATION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTYLEDREPRESENTATION,self).toString()       

        return line
