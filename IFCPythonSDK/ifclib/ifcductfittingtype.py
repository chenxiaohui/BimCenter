#!/usr/bin/python
#coding=utf-8
#Filename:IfcDuctFittingType.py
import log
import common
from ifcflowfittingtype import IFCFLOWFITTINGTYPE

from utils import *

class IFCDUCTFITTINGTYPE(IFCFLOWFITTINGTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCDUCTFITTINGTYPE,self).__init__(id,arg)
        self.type='IFCDUCTFITTINGTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcDuctFittingTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCDUCTFITTINGTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDUCTFITTINGTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDUCTFITTINGTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCDUCTFITTINGTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
