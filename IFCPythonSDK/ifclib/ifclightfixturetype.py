#!/usr/bin/python
#coding=utf-8
#Filename:IfcLightFixtureType.py
import log
import common
from ifcflowterminaltype import IFCFLOWTERMINALTYPE

from utils import *

class IFCLIGHTFIXTURETYPE(IFCFLOWTERMINALTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCLIGHTFIXTURETYPE,self).__init__(id,arg)
        self.type='IFCLIGHTFIXTURETYPE'
        self.inverse={}
        self.PredefinedType=None #IfcLightFixtureTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCLIGHTFIXTURETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLIGHTFIXTURETYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLIGHTFIXTURETYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCLIGHTFIXTURETYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
