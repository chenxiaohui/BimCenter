#!/usr/bin/python
#coding=utf-8
#Filename:IfcDistributionElementType.py
import log
import common
from ifcelementtype import IFCELEMENTTYPE

from utils import *

class IFCDISTRIBUTIONELEMENTTYPE(IFCELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCDISTRIBUTIONELEMENTTYPE,self).__init__(id,arg)
        self.type='IFCDISTRIBUTIONELEMENTTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDISTRIBUTIONELEMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDISTRIBUTIONELEMENTTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDISTRIBUTIONELEMENTTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDISTRIBUTIONELEMENTTYPE,self).toString()       

        return line
