#!/usr/bin/python
#coding=utf-8
#Filename:IfcDistributionChamberElementType.py
import log
import common
from ifcdistributionflowelementtype import IFCDISTRIBUTIONFLOWELEMENTTYPE

from utils import *

class IFCDISTRIBUTIONCHAMBERELEMENTTYPE(IFCDISTRIBUTIONFLOWELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCDISTRIBUTIONCHAMBERELEMENTTYPE,self).__init__(id,arg)
        self.type='IFCDISTRIBUTIONCHAMBERELEMENTTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcDistributionChamberElementTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCDISTRIBUTIONCHAMBERELEMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDISTRIBUTIONCHAMBERELEMENTTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDISTRIBUTIONCHAMBERELEMENTTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCDISTRIBUTIONCHAMBERELEMENTTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
