#!/usr/bin/python
#coding=utf-8
#Filename:IfcFanType.py
import log
import common
from ifcflowmovingdevicetype import IFCFLOWMOVINGDEVICETYPE

from utils import *

class IFCFANTYPE(IFCFLOWMOVINGDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFANTYPE,self).__init__(id,arg)
        self.type='IFCFANTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcFanTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCFANTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFANTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFANTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFANTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
