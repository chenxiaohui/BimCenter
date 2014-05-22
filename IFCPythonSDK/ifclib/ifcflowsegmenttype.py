#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowSegmentType.py
import log
import common
from ifcdistributionflowelementtype import IFCDISTRIBUTIONFLOWELEMENTTYPE

from utils import *

class IFCFLOWSEGMENTTYPE(IFCDISTRIBUTIONFLOWELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWSEGMENTTYPE,self).__init__(id,arg)
        self.type='IFCFLOWSEGMENTTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWSEGMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWSEGMENTTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWSEGMENTTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWSEGMENTTYPE,self).toString()       

        return line
