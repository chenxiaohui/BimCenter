#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowFittingType.py
import log
import common
from ifcdistributionflowelementtype import IFCDISTRIBUTIONFLOWELEMENTTYPE

from utils import *

class IFCFLOWFITTINGTYPE(IFCDISTRIBUTIONFLOWELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWFITTINGTYPE,self).__init__(id,arg)
        self.type='IFCFLOWFITTINGTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWFITTINGTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWFITTINGTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWFITTINGTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWFITTINGTYPE,self).toString()       

        return line
