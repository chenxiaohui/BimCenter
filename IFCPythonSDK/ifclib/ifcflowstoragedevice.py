#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowStorageDevice.py
import log
import common
from ifcdistributionflowelement import IFCDISTRIBUTIONFLOWELEMENT

from utils import *

class IFCFLOWSTORAGEDEVICE(IFCDISTRIBUTIONFLOWELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWSTORAGEDEVICE,self).__init__(id,arg)
        self.type='IFCFLOWSTORAGEDEVICE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWSTORAGEDEVICE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWSTORAGEDEVICE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWSTORAGEDEVICE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWSTORAGEDEVICE,self).toString()       

        return line
