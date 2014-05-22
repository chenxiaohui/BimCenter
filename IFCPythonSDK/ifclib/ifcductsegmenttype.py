#!/usr/bin/python
#coding=utf-8
#Filename:IfcDuctSegmentType.py
import log
import common
from ifcflowsegmenttype import IFCFLOWSEGMENTTYPE

from utils import *

class IFCDUCTSEGMENTTYPE(IFCFLOWSEGMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCDUCTSEGMENTTYPE,self).__init__(id,arg)
        self.type='IFCDUCTSEGMENTTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcDuctSegmentTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCDUCTSEGMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDUCTSEGMENTTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDUCTSEGMENTTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCDUCTSEGMENTTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
