#!/usr/bin/python
#coding=utf-8
#Filename:IfcFillAreaStyle.py
import log
import common
from ifcpresentationstyle import IFCPRESENTATIONSTYLE

from utils import *

class IFCFILLAREASTYLE(IFCPRESENTATIONSTYLE):
    """"""
    def __init__(self,id,arg):
        super(IFCFILLAREASTYLE,self).__init__(id,arg)
        self.type='IFCFILLAREASTYLE'
        self.inverse={}
        self.FillStyles=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCFILLAREASTYLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFILLAREASTYLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FillStyles= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFILLAREASTYLE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFILLAREASTYLE,self).toString()       
        line += listParamToSPF(self.FillStyles,typerefToSPF)+','

        return line
