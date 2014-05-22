#!/usr/bin/python
#coding=utf-8
#Filename:IfcPlateType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCPLATETYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCPLATETYPE,self).__init__(id,arg)
        self.type='IFCPLATETYPE'
        self.inverse={}
        self.PredefinedType=None #IfcPlateTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCPLATETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPLATETYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPLATETYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPLATETYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
