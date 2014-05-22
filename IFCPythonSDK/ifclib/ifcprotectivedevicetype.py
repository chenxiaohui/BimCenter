#!/usr/bin/python
#coding=utf-8
#Filename:IfcProtectiveDeviceType.py
import log
import common
from ifcflowcontrollertype import IFCFLOWCONTROLLERTYPE

from utils import *

class IFCPROTECTIVEDEVICETYPE(IFCFLOWCONTROLLERTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCPROTECTIVEDEVICETYPE,self).__init__(id,arg)
        self.type='IFCPROTECTIVEDEVICETYPE'
        self.inverse={}
        self.PredefinedType=None #IfcProtectiveDeviceTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCPROTECTIVEDEVICETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROTECTIVEDEVICETYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROTECTIVEDEVICETYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPROTECTIVEDEVICETYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
