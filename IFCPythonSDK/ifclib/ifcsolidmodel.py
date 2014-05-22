#!/usr/bin/python
#coding=utf-8
#Filename:IfcSolidModel.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCSOLIDMODEL(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCSOLIDMODEL,self).__init__(id,arg)
        self.type='IFCSOLIDMODEL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSOLIDMODEL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSOLIDMODEL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSOLIDMODEL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSOLIDMODEL,self).toString()       

        return line
