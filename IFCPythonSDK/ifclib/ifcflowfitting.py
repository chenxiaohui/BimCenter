#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowFitting.py
import log
import common
from ifcdistributionflowelement import IFCDISTRIBUTIONFLOWELEMENT

from utils import *

class IFCFLOWFITTING(IFCDISTRIBUTIONFLOWELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWFITTING,self).__init__(id,arg)
        self.type='IFCFLOWFITTING'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWFITTING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWFITTING,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWFITTING,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWFITTING,self).toString()       

        return line
