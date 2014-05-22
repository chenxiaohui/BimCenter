#!/usr/bin/python
#coding=utf-8
#Filename:IfcBuildingElementProxyType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCBUILDINGELEMENTPROXYTYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCBUILDINGELEMENTPROXYTYPE,self).__init__(id,arg)
        self.type='IFCBUILDINGELEMENTPROXYTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcBuildingElementProxyTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCBUILDINGELEMENTPROXYTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBUILDINGELEMENTPROXYTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBUILDINGELEMENTPROXYTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCBUILDINGELEMENTPROXYTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
