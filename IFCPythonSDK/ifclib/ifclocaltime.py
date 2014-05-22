#!/usr/bin/python
#coding=utf-8
#Filename:IfcLocalTime.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCLOCALTIME(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCLOCALTIME,self).__init__(id,arg)
        self.type='IFCLOCALTIME'
        self.inverse={}
        self.HourComponent=None #IfcHourInDay
        self.MinuteComponent=None #IfcMinuteInHour
        self.SecondComponent=None #IfcSecondInMinute
        self.Zone=None #IfcCoordinatedUniversalTimeOffset
        self.DaylightSavingOffset=None #IfcDaylightSavingHour


    def load(self):
        """register inverses"""
        if not super(IFCLOCALTIME,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLOCALTIME,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HourComponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MinuteComponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SecondComponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Zone= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DaylightSavingOffset= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLOCALTIME,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCLOCALTIME,self).toString()       
        line += integerToSPF(self.HourComponent)+','
        line += integerToSPF(self.MinuteComponent)+','
        line += integerToSPF(self.SecondComponent)+','
        line += idToSPF(self.Zone)+','
        line += integerToSPF(self.DaylightSavingOffset)+','

        return line
