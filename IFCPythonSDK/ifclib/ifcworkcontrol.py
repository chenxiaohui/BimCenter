#!/usr/bin/python
#coding=utf-8
#Filename:IfcWorkControl.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCWORKCONTROL(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCWORKCONTROL,self).__init__(id,arg)
        self.type='IFCWORKCONTROL'
        self.inverse={}
        self.Identifier=None #IfcIdentifier
        self.CreationDate=None #IfcDateTimeSelect
        self.Creators=None #SET
        self.Purpose=None #IfcLabel
        self.Duration=None #IfcTimeMeasure
        self.TotalFloat=None #IfcTimeMeasure
        self.StartTime=None #IfcDateTimeSelect
        self.FinishTime=None #IfcDateTimeSelect
        self.WorkControlType=None #IfcWorkControlTypeEnum
        self.UserDefinedControlType=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCWORKCONTROL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWORKCONTROL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Identifier= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CreationDate= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Creators= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Purpose= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Duration= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TotalFloat= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.StartTime= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FinishTime= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WorkControlType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedControlType= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCWORKCONTROL,self).getAttrCount()+10

    def toString(self):
        """"""
        line=super(IFCWORKCONTROL,self).toString()       
        line += strToSPF(self.Identifier)+','
        line += typerefToSPF(self.CreationDate)+','
        line += listParamToSPF(self.Creators,idToSPF)+','
        line += strToSPF(self.Purpose)+','
        line += integerToSPF(self.Duration)+','
        line += integerToSPF(self.TotalFloat)+','
        line += typerefToSPF(self.StartTime)+','
        line += typerefToSPF(self.FinishTime)+','
        line += typerefToSPF(self.WorkControlType)+','
        line += strToSPF(self.UserDefinedControlType)+','

        return line
