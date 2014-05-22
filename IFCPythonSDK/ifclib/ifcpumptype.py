#!/usr/bin/python
#coding=utf-8
#Filename:IfcPumpType.py
import log
import common
from ifcflowmovingdevicetype import IFCFLOWMOVINGDEVICETYPE

from utils import *

class IFCPUMPTYPE(IFCFLOWMOVINGDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCPUMPTYPE,self).__init__(id,arg)
        self.type='IFCPUMPTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcPumpTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCPUMPTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPUMPTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPUMPTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPUMPTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
