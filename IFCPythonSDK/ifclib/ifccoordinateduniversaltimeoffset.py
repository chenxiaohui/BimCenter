#!/usr/bin/python
#coding=utf-8
#Filename:IfcCoordinatedUniversalTimeOffset.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCOORDINATEDUNIVERSALTIMEOFFSET(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCOORDINATEDUNIVERSALTIMEOFFSET,self).__init__(id,arg)
        self.type='IFCCOORDINATEDUNIVERSALTIMEOFFSET'
        self.inverse={}
        self.HourOffset=None #IfcHourInDay
        self.MinuteOffset=None #IfcMinuteInHour
        self.Sense=None #IfcAheadOrBehind


    def load(self):
        """register inverses"""
        if not super(IFCCOORDINATEDUNIVERSALTIMEOFFSET,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOORDINATEDUNIVERSALTIMEOFFSET,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HourOffset= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MinuteOffset= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Sense= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOORDINATEDUNIVERSALTIMEOFFSET,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCCOORDINATEDUNIVERSALTIMEOFFSET,self).toString()       
        line += integerToSPF(self.HourOffset)+','
        line += integerToSPF(self.MinuteOffset)+','
        line += typerefToSPF(self.Sense)+','

        return line
