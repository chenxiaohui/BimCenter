#!/usr/bin/python
#coding=utf-8
#Filename:IfcDateAndTime.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCDATEANDTIME(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCDATEANDTIME,self).__init__(id,arg)
        self.type='IFCDATEANDTIME'
        self.inverse={}
        self.DateComponent=None #IfcCalendarDate
        self.TimeComponent=None #IfcLocalTime


    def load(self):
        """register inverses"""
        if not super(IFCDATEANDTIME,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDATEANDTIME,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DateComponent= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TimeComponent= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDATEANDTIME,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCDATEANDTIME,self).toString()       
        line += idToSPF(self.DateComponent)+','
        line += idToSPF(self.TimeComponent)+','

        return line
