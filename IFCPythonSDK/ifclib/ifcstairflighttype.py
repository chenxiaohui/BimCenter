#!/usr/bin/python
#coding=utf-8
#Filename:IfcStairFlightType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCSTAIRFLIGHTTYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCSTAIRFLIGHTTYPE,self).__init__(id,arg)
        self.type='IFCSTAIRFLIGHTTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcStairFlightTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSTAIRFLIGHTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTAIRFLIGHTTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTAIRFLIGHTTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSTAIRFLIGHTTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
