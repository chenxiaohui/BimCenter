#!/usr/bin/python
#coding=utf-8
#Filename:IfcBeamType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCBEAMTYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCBEAMTYPE,self).__init__(id,arg)
        self.type='IFCBEAMTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcBeamTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCBEAMTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBEAMTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBEAMTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCBEAMTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
