#!/usr/bin/python
#coding=utf-8
#Filename:IfcStackTerminalType.py
import log
import common
from ifcflowterminaltype import IFCFLOWTERMINALTYPE

from utils import *

class IFCSTACKTERMINALTYPE(IFCFLOWTERMINALTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCSTACKTERMINALTYPE,self).__init__(id,arg)
        self.type='IFCSTACKTERMINALTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcStackTerminalTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSTACKTERMINALTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTACKTERMINALTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTACKTERMINALTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSTACKTERMINALTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
