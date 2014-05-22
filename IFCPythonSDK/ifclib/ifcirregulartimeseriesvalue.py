#!/usr/bin/python
#coding=utf-8
#Filename:IfcIrregularTimeSeriesValue.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCIRREGULARTIMESERIESVALUE(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCIRREGULARTIMESERIESVALUE,self).__init__(id,arg)
        self.type='IFCIRREGULARTIMESERIESVALUE'
        self.inverse={}
        self.TimeStamp=None #IfcDateTimeSelect
        self.ListValues=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCIRREGULARTIMESERIESVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCIRREGULARTIMESERIESVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TimeStamp= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ListValues= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCIRREGULARTIMESERIESVALUE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCIRREGULARTIMESERIESVALUE,self).toString()       
        line += typerefToSPF(self.TimeStamp)+','
        line += listParamToSPF(self.ListValues,typerefToSPF)+','

        return line
