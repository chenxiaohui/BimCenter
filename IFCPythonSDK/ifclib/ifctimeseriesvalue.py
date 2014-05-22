#!/usr/bin/python
#coding=utf-8
#Filename:IfcTimeSeriesValue.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCTIMESERIESVALUE(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCTIMESERIESVALUE,self).__init__(id,arg)
        self.type='IFCTIMESERIESVALUE'
        self.inverse={}
        self.ListValues=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCTIMESERIESVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTIMESERIESVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ListValues= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTIMESERIESVALUE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCTIMESERIESVALUE,self).toString()       
        line += listParamToSPF(self.ListValues,typerefToSPF)+','

        return line
