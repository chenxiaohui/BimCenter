#!/usr/bin/python
#coding=utf-8
#Filename:IfcCableCarrierSegmentType.py
import log
import common
from ifcflowsegmenttype import IFCFLOWSEGMENTTYPE

from utils import *

class IFCCABLECARRIERSEGMENTTYPE(IFCFLOWSEGMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCABLECARRIERSEGMENTTYPE,self).__init__(id,arg)
        self.type='IFCCABLECARRIERSEGMENTTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcCableCarrierSegmentTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCABLECARRIERSEGMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCABLECARRIERSEGMENTTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCABLECARRIERSEGMENTTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCABLECARRIERSEGMENTTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
