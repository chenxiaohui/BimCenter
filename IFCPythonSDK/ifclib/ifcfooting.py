#!/usr/bin/python
#coding=utf-8
#Filename:IfcFooting.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCFOOTING(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFOOTING,self).__init__(id,arg)
        self.type='IFCFOOTING'
        self.inverse={}
        self.PredefinedType=None #IfcFootingTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCFOOTING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFOOTING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFOOTING,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFOOTING,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
