#!/usr/bin/python
#coding=utf-8
#Filename:IfcTimeSeries.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCTIMESERIES(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCTIMESERIES,self).__init__(id,arg)
        self.type='IFCTIMESERIES'
        self.inverse={}
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.StartTime=None #IfcDateTimeSelect
        self.EndTime=None #IfcDateTimeSelect
        self.TimeSeriesDataType=None #IfcTimeSeriesDataTypeEnum
        self.DataOrigin=None #IfcDataOriginEnum
        self.UserDefinedDataOrigin=None #IfcLabel
        self.Unit=None #IfcUnit
        self.inverse['DocumentedBy']=[] #inverse:SET of IfcTimeSeriesReferenceRelationship


    def load(self):
        """register inverses"""
        if not super(IFCTIMESERIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTIMESERIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.StartTime= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EndTime= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TimeSeriesDataType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DataOrigin= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedDataOrigin= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Unit= spfToTypeRef(arg)

        inverses = self.args.getInverses('IFCTIMESERIESREFERENCERELATIONSHIP', 'ReferencedTimeSeries');
        if inverses:
            self.inverse['DocumentedBy']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTIMESERIES,self).getAttrCount()+8

    def toString(self):
        """"""
        line=super(IFCTIMESERIES,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += typerefToSPF(self.StartTime)+','
        line += typerefToSPF(self.EndTime)+','
        line += typerefToSPF(self.TimeSeriesDataType)+','
        line += typerefToSPF(self.DataOrigin)+','
        line += strToSPF(self.UserDefinedDataOrigin)+','
        line += typerefToSPF(self.Unit)+','

        return line
