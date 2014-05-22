#!/usr/bin/python
#coding=utf-8
#Filename:IfcElectricTimeControlType.py
import log
import common
from ifcflowcontrollertype import IFCFLOWCONTROLLERTYPE

from utils import *

class IFCELECTRICTIMECONTROLTYPE(IFCFLOWCONTROLLERTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCELECTRICTIMECONTROLTYPE,self).__init__(id,arg)
        self.type='IFCELECTRICTIMECONTROLTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcElectricTimeControlTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCELECTRICTIMECONTROLTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELECTRICTIMECONTROLTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELECTRICTIMECONTROLTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCELECTRICTIMECONTROLTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
