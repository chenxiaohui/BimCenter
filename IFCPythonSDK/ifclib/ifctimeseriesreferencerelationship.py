#!/usr/bin/python
#coding=utf-8
#Filename:IfcTimeSeriesReferenceRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCTIMESERIESREFERENCERELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCTIMESERIESREFERENCERELATIONSHIP,self).__init__(id,arg)
        self.type='IFCTIMESERIESREFERENCERELATIONSHIP'
        self.inverse={}
        self.ReferencedTimeSeries=None #IfcTimeSeries
        self.TimeSeriesReferences=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCTIMESERIESREFERENCERELATIONSHIP,self).load():
            return False
        idx=super(IFCTIMESERIESREFERENCERELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcTimeSeriesReferenceRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcTimeSeriesReferenceRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCTIMESERIESREFERENCERELATIONSHIP','ReferencedTimeSeries',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTIMESERIESREFERENCERELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ReferencedTimeSeries= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TimeSeriesReferences= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTIMESERIESREFERENCERELATIONSHIP,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCTIMESERIESREFERENCERELATIONSHIP,self).toString()       
        line += idToSPF(self.ReferencedTimeSeries)+','
        line += listParamToSPF(self.TimeSeriesReferences,typerefToSPF)+','

        return line
