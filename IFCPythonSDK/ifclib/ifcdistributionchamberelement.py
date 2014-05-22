#!/usr/bin/python
#coding=utf-8
#Filename:IfcDistributionChamberElement.py
import log
import common
from ifcdistributionflowelement import IFCDISTRIBUTIONFLOWELEMENT

from utils import *

class IFCDISTRIBUTIONCHAMBERELEMENT(IFCDISTRIBUTIONFLOWELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCDISTRIBUTIONCHAMBERELEMENT,self).__init__(id,arg)
        self.type='IFCDISTRIBUTIONCHAMBERELEMENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDISTRIBUTIONCHAMBERELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDISTRIBUTIONCHAMBERELEMENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDISTRIBUTIONCHAMBERELEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDISTRIBUTIONCHAMBERELEMENT,self).toString()       

        return line
