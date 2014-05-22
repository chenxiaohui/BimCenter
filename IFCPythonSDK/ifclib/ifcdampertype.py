#!/usr/bin/python
#coding=utf-8
#Filename:IfcDamperType.py
import log
import common
from ifcflowcontrollertype import IFCFLOWCONTROLLERTYPE

from utils import *

class IFCDAMPERTYPE(IFCFLOWCONTROLLERTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCDAMPERTYPE,self).__init__(id,arg)
        self.type='IFCDAMPERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcDamperTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCDAMPERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDAMPERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDAMPERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCDAMPERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
