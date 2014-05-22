#!/usr/bin/python
#coding=utf-8
#Filename:IfcElectricalElement.py
import log
import common
from ifcelement import IFCELEMENT

from utils import *

class IFCELECTRICALELEMENT(IFCELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCELECTRICALELEMENT,self).__init__(id,arg)
        self.type='IFCELECTRICALELEMENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCELECTRICALELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELECTRICALELEMENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELECTRICALELEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCELECTRICALELEMENT,self).toString()       

        return line
