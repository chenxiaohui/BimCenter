#!/usr/bin/python
#coding=utf-8
#Filename:IfcElectricHeaterType.py
import log
import common
from ifcflowterminaltype import IFCFLOWTERMINALTYPE

from utils import *

class IFCELECTRICHEATERTYPE(IFCFLOWTERMINALTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCELECTRICHEATERTYPE,self).__init__(id,arg)
        self.type='IFCELECTRICHEATERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcElectricHeaterTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCELECTRICHEATERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELECTRICHEATERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELECTRICHEATERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCELECTRICHEATERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
