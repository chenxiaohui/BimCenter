#!/usr/bin/python
#coding=utf-8
#Filename:IfcDistributionFlowElementType.py
import log
import common
from ifcdistributionelementtype import IFCDISTRIBUTIONELEMENTTYPE

from utils import *

class IFCDISTRIBUTIONFLOWELEMENTTYPE(IFCDISTRIBUTIONELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCDISTRIBUTIONFLOWELEMENTTYPE,self).__init__(id,arg)
        self.type='IFCDISTRIBUTIONFLOWELEMENTTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDISTRIBUTIONFLOWELEMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDISTRIBUTIONFLOWELEMENTTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDISTRIBUTIONFLOWELEMENTTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDISTRIBUTIONFLOWELEMENTTYPE,self).toString()       

        return line
