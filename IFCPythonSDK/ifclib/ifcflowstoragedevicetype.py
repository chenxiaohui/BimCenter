#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowStorageDeviceType.py
import log
import common
from ifcdistributionflowelementtype import IFCDISTRIBUTIONFLOWELEMENTTYPE

from utils import *

class IFCFLOWSTORAGEDEVICETYPE(IFCDISTRIBUTIONFLOWELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWSTORAGEDEVICETYPE,self).__init__(id,arg)
        self.type='IFCFLOWSTORAGEDEVICETYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWSTORAGEDEVICETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWSTORAGEDEVICETYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWSTORAGEDEVICETYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWSTORAGEDEVICETYPE,self).toString()       

        return line
