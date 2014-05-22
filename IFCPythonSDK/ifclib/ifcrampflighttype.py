#!/usr/bin/python
#coding=utf-8
#Filename:IfcRampFlightType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCRAMPFLIGHTTYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCRAMPFLIGHTTYPE,self).__init__(id,arg)
        self.type='IFCRAMPFLIGHTTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcRampFlightTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCRAMPFLIGHTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRAMPFLIGHTTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRAMPFLIGHTTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRAMPFLIGHTTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
