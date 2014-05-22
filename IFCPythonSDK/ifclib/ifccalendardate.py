#!/usr/bin/python
#coding=utf-8
#Filename:IfcCalendarDate.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCALENDARDATE(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCALENDARDATE,self).__init__(id,arg)
        self.type='IFCCALENDARDATE'
        self.inverse={}
        self.DayComponent=None #IfcDayInMonthNumber
        self.MonthComponent=None #IfcMonthInYearNumber
        self.YearComponent=None #IfcYearNumber


    def load(self):
        """register inverses"""
        if not super(IFCCALENDARDATE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCALENDARDATE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DayComponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MonthComponent= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.YearComponent= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCALENDARDATE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCCALENDARDATE,self).toString()       
        line += integerToSPF(self.DayComponent)+','
        line += integerToSPF(self.MonthComponent)+','
        line += integerToSPF(self.YearComponent)+','

        return line
