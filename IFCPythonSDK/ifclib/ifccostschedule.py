#!/usr/bin/python
#coding=utf-8
#Filename:IfcCostSchedule.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCCOSTSCHEDULE(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCCOSTSCHEDULE,self).__init__(id,arg)
        self.type='IFCCOSTSCHEDULE'
        self.inverse={}
        self.SubmittedBy=None #IfcActorSelect
        self.PreparedBy=None #IfcActorSelect
        self.SubmittedOn=None #IfcDateTimeSelect
        self.Status=None #IfcLabel
        self.TargetUsers=None #SET
        self.UpdateDate=None #IfcDateTimeSelect
        self.ID=None #IfcIdentifier
        self.PredefinedType=None #IfcCostScheduleTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCOSTSCHEDULE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOSTSCHEDULE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SubmittedBy= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PreparedBy= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SubmittedOn= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Status= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TargetUsers= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UpdateDate= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ID= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOSTSCHEDULE,self).getAttrCount()+8

    def toString(self):
        """"""
        line=super(IFCCOSTSCHEDULE,self).toString()       
        line += typerefToSPF(self.SubmittedBy)+','
        line += typerefToSPF(self.PreparedBy)+','
        line += typerefToSPF(self.SubmittedOn)+','
        line += strToSPF(self.Status)+','
        line += listParamToSPF(self.TargetUsers,typerefToSPF)+','
        line += typerefToSPF(self.UpdateDate)+','
        line += strToSPF(self.ID)+','
        line += typerefToSPF(self.PredefinedType)+','

        return line
