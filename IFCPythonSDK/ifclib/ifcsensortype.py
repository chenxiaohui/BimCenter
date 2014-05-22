#!/usr/bin/python
#coding=utf-8
#Filename:IfcSensorType.py
import log
import common
from ifcdistributioncontrolelementtype import IFCDISTRIBUTIONCONTROLELEMENTTYPE

from utils import *

class IFCSENSORTYPE(IFCDISTRIBUTIONCONTROLELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCSENSORTYPE,self).__init__(id,arg)
        self.type='IFCSENSORTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcSensorTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSENSORTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSENSORTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSENSORTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSENSORTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
