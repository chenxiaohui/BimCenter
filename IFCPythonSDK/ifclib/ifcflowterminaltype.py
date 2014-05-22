#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowTerminalType.py
import log
import common
from ifcdistributionflowelementtype import IFCDISTRIBUTIONFLOWELEMENTTYPE

from utils import *

class IFCFLOWTERMINALTYPE(IFCDISTRIBUTIONFLOWELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWTERMINALTYPE,self).__init__(id,arg)
        self.type='IFCFLOWTERMINALTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWTERMINALTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWTERMINALTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWTERMINALTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWTERMINALTYPE,self).toString()       

        return line
