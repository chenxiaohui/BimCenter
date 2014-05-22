#!/usr/bin/python
#coding=utf-8
#Filename:IfcCableCarrierFittingType.py
import log
import common
from ifcflowfittingtype import IFCFLOWFITTINGTYPE

from utils import *

class IFCCABLECARRIERFITTINGTYPE(IFCFLOWFITTINGTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCABLECARRIERFITTINGTYPE,self).__init__(id,arg)
        self.type='IFCCABLECARRIERFITTINGTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcCableCarrierFittingTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCABLECARRIERFITTINGTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCABLECARRIERFITTINGTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCABLECARRIERFITTINGTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCABLECARRIERFITTINGTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
