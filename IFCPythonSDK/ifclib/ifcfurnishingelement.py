#!/usr/bin/python
#coding=utf-8
#Filename:IfcFurnishingElement.py
import log
import common
from ifcelement import IFCELEMENT

from utils import *

class IFCFURNISHINGELEMENT(IFCELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFURNISHINGELEMENT,self).__init__(id,arg)
        self.type='IFCFURNISHINGELEMENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFURNISHINGELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFURNISHINGELEMENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFURNISHINGELEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFURNISHINGELEMENT,self).toString()       

        return line
