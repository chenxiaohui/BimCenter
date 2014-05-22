#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowInstrumentType.py
import log
import common
from ifcdistributioncontrolelementtype import IFCDISTRIBUTIONCONTROLELEMENTTYPE

from utils import *

class IFCFLOWINSTRUMENTTYPE(IFCDISTRIBUTIONCONTROLELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWINSTRUMENTTYPE,self).__init__(id,arg)
        self.type='IFCFLOWINSTRUMENTTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcFlowInstrumentTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCFLOWINSTRUMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWINSTRUMENTTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWINSTRUMENTTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFLOWINSTRUMENTTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
