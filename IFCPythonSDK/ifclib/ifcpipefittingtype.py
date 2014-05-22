#!/usr/bin/python
#coding=utf-8
#Filename:IfcPipeFittingType.py
import log
import common
from ifcflowfittingtype import IFCFLOWFITTINGTYPE

from utils import *

class IFCPIPEFITTINGTYPE(IFCFLOWFITTINGTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCPIPEFITTINGTYPE,self).__init__(id,arg)
        self.type='IFCPIPEFITTINGTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcPipeFittingTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCPIPEFITTINGTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPIPEFITTINGTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPIPEFITTINGTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPIPEFITTINGTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
