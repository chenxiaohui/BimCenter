#!/usr/bin/python
#coding=utf-8
#Filename:IfcSanitaryTerminalType.py
import log
import common
from ifcflowterminaltype import IFCFLOWTERMINALTYPE

from utils import *

class IFCSANITARYTERMINALTYPE(IFCFLOWTERMINALTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCSANITARYTERMINALTYPE,self).__init__(id,arg)
        self.type='IFCSANITARYTERMINALTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcSanitaryTerminalTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSANITARYTERMINALTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSANITARYTERMINALTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSANITARYTERMINALTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSANITARYTERMINALTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
