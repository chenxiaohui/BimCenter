#!/usr/bin/python
#coding=utf-8
#Filename:IfcWasteTerminalType.py
import log
import common
from ifcflowterminaltype import IFCFLOWTERMINALTYPE

from utils import *

class IFCWASTETERMINALTYPE(IFCFLOWTERMINALTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCWASTETERMINALTYPE,self).__init__(id,arg)
        self.type='IFCWASTETERMINALTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcWasteTerminalTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCWASTETERMINALTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWASTETERMINALTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCWASTETERMINALTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCWASTETERMINALTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
