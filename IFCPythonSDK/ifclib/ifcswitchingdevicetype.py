#!/usr/bin/python
#coding=utf-8
#Filename:IfcSwitchingDeviceType.py
import log
import common
from ifcflowcontrollertype import IFCFLOWCONTROLLERTYPE

from utils import *

class IFCSWITCHINGDEVICETYPE(IFCFLOWCONTROLLERTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCSWITCHINGDEVICETYPE,self).__init__(id,arg)
        self.type='IFCSWITCHINGDEVICETYPE'
        self.inverse={}
        self.PredefinedType=None #IfcSwitchingDeviceTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSWITCHINGDEVICETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSWITCHINGDEVICETYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSWITCHINGDEVICETYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSWITCHINGDEVICETYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
