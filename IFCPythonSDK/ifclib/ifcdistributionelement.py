#!/usr/bin/python
#coding=utf-8
#Filename:IfcDistributionElement.py
import log
import common
from ifcelement import IFCELEMENT

from utils import *

class IFCDISTRIBUTIONELEMENT(IFCELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCDISTRIBUTIONELEMENT,self).__init__(id,arg)
        self.type='IFCDISTRIBUTIONELEMENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDISTRIBUTIONELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDISTRIBUTIONELEMENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDISTRIBUTIONELEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDISTRIBUTIONELEMENT,self).toString()       

        return line
