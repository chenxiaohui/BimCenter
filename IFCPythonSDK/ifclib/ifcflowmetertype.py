#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowMeterType.py
import log
import common
from ifcflowcontrollertype import IFCFLOWCONTROLLERTYPE

from utils import *

class IFCFLOWMETERTYPE(IFCFLOWCONTROLLERTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWMETERTYPE,self).__init__(id,arg)
        self.type='IFCFLOWMETERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcFlowMeterTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCFLOWMETERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWMETERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWMETERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFLOWMETERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
