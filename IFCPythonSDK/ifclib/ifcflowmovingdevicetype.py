#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowMovingDeviceType.py
import log
import common
from ifcdistributionflowelementtype import IFCDISTRIBUTIONFLOWELEMENTTYPE

from utils import *

class IFCFLOWMOVINGDEVICETYPE(IFCDISTRIBUTIONFLOWELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWMOVINGDEVICETYPE,self).__init__(id,arg)
        self.type='IFCFLOWMOVINGDEVICETYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWMOVINGDEVICETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWMOVINGDEVICETYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWMOVINGDEVICETYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWMOVINGDEVICETYPE,self).toString()       

        return line
