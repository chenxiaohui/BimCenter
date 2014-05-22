#!/usr/bin/python
#coding=utf-8
#Filename:IfcSlab.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCSLAB(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCSLAB,self).__init__(id,arg)
        self.type='IFCSLAB'
        self.inverse={}
        self.PredefinedType=None #IfcSlabTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSLAB,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSLAB,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSLAB,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSLAB,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
