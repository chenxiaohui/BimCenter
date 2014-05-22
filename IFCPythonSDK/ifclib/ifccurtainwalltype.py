#!/usr/bin/python
#coding=utf-8
#Filename:IfcCurtainWallType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCCURTAINWALLTYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCURTAINWALLTYPE,self).__init__(id,arg)
        self.type='IFCCURTAINWALLTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcCurtainWallTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCURTAINWALLTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCURTAINWALLTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCURTAINWALLTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCURTAINWALLTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
