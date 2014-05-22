#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowSegment.py
import log
import common
from ifcdistributionflowelement import IFCDISTRIBUTIONFLOWELEMENT

from utils import *

class IFCFLOWSEGMENT(IFCDISTRIBUTIONFLOWELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWSEGMENT,self).__init__(id,arg)
        self.type='IFCFLOWSEGMENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWSEGMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWSEGMENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWSEGMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWSEGMENT,self).toString()       

        return line
