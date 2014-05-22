#!/usr/bin/python
#coding=utf-8
#Filename:IfcCoveringType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCCOVERINGTYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCOVERINGTYPE,self).__init__(id,arg)
        self.type='IFCCOVERINGTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcCoveringTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCOVERINGTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOVERINGTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOVERINGTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCOVERINGTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
