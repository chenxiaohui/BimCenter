#!/usr/bin/python
#coding=utf-8
#Filename:IfcActuatorType.py
import log
import common
from ifcdistributioncontrolelementtype import IFCDISTRIBUTIONCONTROLELEMENTTYPE

from utils import *

class IFCACTUATORTYPE(IFCDISTRIBUTIONCONTROLELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCACTUATORTYPE,self).__init__(id,arg)
        self.type='IFCACTUATORTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcActuatorTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCACTUATORTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCACTUATORTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCACTUATORTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCACTUATORTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
