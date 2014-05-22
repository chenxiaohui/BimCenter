#!/usr/bin/python
#coding=utf-8
#Filename:IfcDistributionPort.py
import log
import common
from ifcport import IFCPORT

from utils import *

class IFCDISTRIBUTIONPORT(IFCPORT):
    """"""
    def __init__(self,id,arg):
        super(IFCDISTRIBUTIONPORT,self).__init__(id,arg)
        self.type='IFCDISTRIBUTIONPORT'
        self.inverse={}
        self.FlowDirection=None #IfcFlowDirectionEnum


    def load(self):
        """register inverses"""
        if not super(IFCDISTRIBUTIONPORT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDISTRIBUTIONPORT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FlowDirection= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDISTRIBUTIONPORT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCDISTRIBUTIONPORT,self).toString()       
        line += typerefToSPF(self.FlowDirection)+','

        return line
