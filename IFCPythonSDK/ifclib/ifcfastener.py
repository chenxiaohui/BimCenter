#!/usr/bin/python
#coding=utf-8
#Filename:IfcFastener.py
import log
import common
from ifcelementcomponent import IFCELEMENTCOMPONENT

from utils import *

class IFCFASTENER(IFCELEMENTCOMPONENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFASTENER,self).__init__(id,arg)
        self.type='IFCFASTENER'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFASTENER,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFASTENER,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFASTENER,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFASTENER,self).toString()       

        return line
