#!/usr/bin/python
#coding=utf-8
#Filename:IfcWallType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCWALLTYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCWALLTYPE,self).__init__(id,arg)
        self.type='IFCWALLTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcWallTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCWALLTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWALLTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCWALLTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCWALLTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
