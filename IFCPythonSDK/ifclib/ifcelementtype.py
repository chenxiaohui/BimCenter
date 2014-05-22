#!/usr/bin/python
#coding=utf-8
#Filename:IfcElementType.py
import log
import common
from ifctypeproduct import IFCTYPEPRODUCT

from utils import *

class IFCELEMENTTYPE(IFCTYPEPRODUCT):
    """"""
    def __init__(self,id,arg):
        super(IFCELEMENTTYPE,self).__init__(id,arg)
        self.type='IFCELEMENTTYPE'
        self.inverse={}
        self.ElementType=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCELEMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELEMENTTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ElementType= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELEMENTTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCELEMENTTYPE,self).toString()       
        line += strToSPF(self.ElementType)+','

        return line
