#!/usr/bin/python
#coding=utf-8
#Filename:IfcPipeSegmentType.py
import log
import common
from ifcflowsegmenttype import IFCFLOWSEGMENTTYPE

from utils import *

class IFCPIPESEGMENTTYPE(IFCFLOWSEGMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCPIPESEGMENTTYPE,self).__init__(id,arg)
        self.type='IFCPIPESEGMENTTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcPipeSegmentTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCPIPESEGMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPIPESEGMENTTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPIPESEGMENTTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPIPESEGMENTTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
