#!/usr/bin/python
#coding=utf-8
#Filename:IfcScheduleTimeControl.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCSCHEDULETIMECONTROL(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCSCHEDULETIMECONTROL,self).__init__(id,arg)
        self.type='IFCSCHEDULETIMECONTROL'
        self.inverse={}
        self.ActualStart=None #IfcDateTimeSelect
        self.EarlyStart=None #IfcDateTimeSelect
        self.LateStart=None #IfcDateTimeSelect
        self.ScheduleStart=None #IfcDateTimeSelect
        self.ActualFinish=None #IfcDateTimeSelect
        self.EarlyFinish=None #IfcDateTimeSelect
        self.LateFinish=None #IfcDateTimeSelect
        self.ScheduleFinish=None #IfcDateTimeSelect
        self.ScheduleDuration=None #IfcTimeMeasure
        self.ActualDuration=None #IfcTimeMeasure
        self.RemainingTime=None #IfcTimeMeasure
        self.FreeFloat=None #IfcTimeMeasure
        self.TotalFloat=None #IfcTimeMeasure
        self.IsCritical=None #BOOLEAN
        self.StatusTime=None #IfcDateTimeSelect
        self.StartFloat=None #IfcTimeMeasure
        self.FinishFloat=None #IfcTimeMeasure
        self.Completion=None #IfcPositiveRatioMeasure
        self.inverse['ScheduleTimeControlAssigned']=[] #inverse:IfcRelAssignsTasks of Alone


    def load(self):
        """register inverses"""
        if not super(IFCSCHEDULETIMECONTROL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSCHEDULETIMECONTROL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ActualStart= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EarlyStart= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LateStart= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ScheduleStart= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ActualFinish= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EarlyFinish= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LateFinish= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ScheduleFinish= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ScheduleDuration= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ActualDuration= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RemainingTime= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FreeFloat= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TotalFloat= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.IsCritical= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.StatusTime= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.StartFloat= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FinishFloat= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Completion= spfToInteger(arg)

        inverses = self.args.getInverses('IFCRELASSIGNSTASKS', 'TimeForTask');
        if inverses:
            self.inverse['ScheduleTimeControlAssigned']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSCHEDULETIMECONTROL,self).getAttrCount()+18

    def toString(self):
        """"""
        line=super(IFCSCHEDULETIMECONTROL,self).toString()       
        line += typerefToSPF(self.ActualStart)+','
        line += typerefToSPF(self.EarlyStart)+','
        line += typerefToSPF(self.LateStart)+','
        line += typerefToSPF(self.ScheduleStart)+','
        line += typerefToSPF(self.ActualFinish)+','
        line += typerefToSPF(self.EarlyFinish)+','
        line += typerefToSPF(self.LateFinish)+','
        line += typerefToSPF(self.ScheduleFinish)+','
        line += integerToSPF(self.ScheduleDuration)+','
        line += integerToSPF(self.ActualDuration)+','
        line += integerToSPF(self.RemainingTime)+','
        line += integerToSPF(self.FreeFloat)+','
        line += integerToSPF(self.TotalFloat)+','
        line += logicalToSPF(self.IsCritical)+','
        line += typerefToSPF(self.StatusTime)+','
        line += integerToSPF(self.StartFloat)+','
        line += integerToSPF(self.FinishFloat)+','
        line += integerToSPF(self.Completion)+','

        return line
