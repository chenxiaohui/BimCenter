#!/usr/bin/python
#coding=utf-8
#Filename:IfcTransportElementType.py
import log
import common
from ifcelementtype import IFCELEMENTTYPE

from utils import *

class IFCTRANSPORTELEMENTTYPE(IFCELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCTRANSPORTELEMENTTYPE,self).__init__(id,arg)
        self.type='IFCTRANSPORTELEMENTTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcTransportElementTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCTRANSPORTELEMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTRANSPORTELEMENTTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTRANSPORTELEMENTTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCTRANSPORTELEMENTTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
