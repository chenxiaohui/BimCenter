#!/usr/bin/python
#coding=utf-8
#Filename:IfcCableSegmentType.py
import log
import common
from ifcflowsegmenttype import IFCFLOWSEGMENTTYPE

from utils import *

class IFCCABLESEGMENTTYPE(IFCFLOWSEGMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCABLESEGMENTTYPE,self).__init__(id,arg)
        self.type='IFCCABLESEGMENTTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcCableSegmentTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCABLESEGMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCABLESEGMENTTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCABLESEGMENTTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCABLESEGMENTTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
