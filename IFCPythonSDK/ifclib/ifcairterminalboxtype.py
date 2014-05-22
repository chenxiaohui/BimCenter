#!/usr/bin/python
#coding=utf-8
#Filename:IfcAirTerminalBoxType.py
import log
import common
from ifcflowcontrollertype import IFCFLOWCONTROLLERTYPE

from utils import *

class IFCAIRTERMINALBOXTYPE(IFCFLOWCONTROLLERTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCAIRTERMINALBOXTYPE,self).__init__(id,arg)
        self.type='IFCAIRTERMINALBOXTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcAirTerminalBoxTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCAIRTERMINALBOXTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAIRTERMINALBOXTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAIRTERMINALBOXTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCAIRTERMINALBOXTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
