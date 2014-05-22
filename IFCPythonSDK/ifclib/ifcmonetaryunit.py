#!/usr/bin/python
#coding=utf-8
#Filename:IfcMonetaryUnit.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCMONETARYUNIT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCMONETARYUNIT,self).__init__(id,arg)
        self.type='IFCMONETARYUNIT'
        self.inverse={}
        self.Currency=None #IfcCurrencyEnum


    def load(self):
        """register inverses"""
        if not super(IFCMONETARYUNIT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMONETARYUNIT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Currency= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMONETARYUNIT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCMONETARYUNIT,self).toString()       
        line += typerefToSPF(self.Currency)+','

        return line
