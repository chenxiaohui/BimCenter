#!/usr/bin/python
#coding=utf-8
#Filename:IfcCompressorType.py
import log
import common
from ifcflowmovingdevicetype import IFCFLOWMOVINGDEVICETYPE

from utils import *

class IFCCOMPRESSORTYPE(IFCFLOWMOVINGDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCOMPRESSORTYPE,self).__init__(id,arg)
        self.type='IFCCOMPRESSORTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcCompressorTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCOMPRESSORTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOMPRESSORTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOMPRESSORTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCOMPRESSORTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
