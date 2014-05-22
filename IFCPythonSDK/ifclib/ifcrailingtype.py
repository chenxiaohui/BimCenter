#!/usr/bin/python
#coding=utf-8
#Filename:IfcRailingType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCRAILINGTYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCRAILINGTYPE,self).__init__(id,arg)
        self.type='IFCRAILINGTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcRailingTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCRAILINGTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRAILINGTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRAILINGTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRAILINGTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
