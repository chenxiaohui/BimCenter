#!/usr/bin/python
#coding=utf-8
#Filename:IfcTimeSeriesSchedule.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCTIMESERIESSCHEDULE(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCTIMESERIESSCHEDULE,self).__init__(id,arg)
        self.type='IFCTIMESERIESSCHEDULE'
        self.inverse={}
        self.ApplicableDates=None #LIST
        self.TimeSeriesScheduleType=None #IfcTimeSeriesScheduleTypeEnum
        self.TimeSeries=None #IfcTimeSeries


    def load(self):
        """register inverses"""
        if not super(IFCTIMESERIESSCHEDULE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTIMESERIESSCHEDULE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApplicableDates= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TimeSeriesScheduleType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TimeSeries= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTIMESERIESSCHEDULE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCTIMESERIESSCHEDULE,self).toString()       
        line += listParamToSPF(self.ApplicableDates,typerefToSPF)+','
        line += typerefToSPF(self.TimeSeriesScheduleType)+','
        line += idToSPF(self.TimeSeries)+','

        return line
