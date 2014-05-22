#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowControllerType.py
import log
import common
from ifcdistributionflowelementtype import IFCDISTRIBUTIONFLOWELEMENTTYPE

from utils import *

class IFCFLOWCONTROLLERTYPE(IFCDISTRIBUTIONFLOWELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWCONTROLLERTYPE,self).__init__(id,arg)
        self.type='IFCFLOWCONTROLLERTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWCONTROLLERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWCONTROLLERTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWCONTROLLERTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWCONTROLLERTYPE,self).toString()       

        return line
