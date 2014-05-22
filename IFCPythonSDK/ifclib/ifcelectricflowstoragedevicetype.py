#!/usr/bin/python
#coding=utf-8
#Filename:IfcElectricFlowStorageDeviceType.py
import log
import common
from ifcflowstoragedevicetype import IFCFLOWSTORAGEDEVICETYPE

from utils import *

class IFCELECTRICFLOWSTORAGEDEVICETYPE(IFCFLOWSTORAGEDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCELECTRICFLOWSTORAGEDEVICETYPE,self).__init__(id,arg)
        self.type='IFCELECTRICFLOWSTORAGEDEVICETYPE'
        self.inverse={}
        self.PredefinedType=None #IfcElectricFlowStorageDeviceTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCELECTRICFLOWSTORAGEDEVICETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELECTRICFLOWSTORAGEDEVICETYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELECTRICFLOWSTORAGEDEVICETYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCELECTRICFLOWSTORAGEDEVICETYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
