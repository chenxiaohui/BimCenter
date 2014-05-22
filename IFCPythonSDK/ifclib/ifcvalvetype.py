#!/usr/bin/python
#coding=utf-8
#Filename:IfcValveType.py
import log
import common
from ifcflowcontrollertype import IFCFLOWCONTROLLERTYPE

from utils import *

class IFCVALVETYPE(IFCFLOWCONTROLLERTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCVALVETYPE,self).__init__(id,arg)
        self.type='IFCVALVETYPE'
        self.inverse={}
        self.PredefinedType=None #IfcValveTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCVALVETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCVALVETYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCVALVETYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCVALVETYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
