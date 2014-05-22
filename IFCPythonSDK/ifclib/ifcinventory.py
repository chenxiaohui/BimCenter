#!/usr/bin/python
#coding=utf-8
#Filename:IfcInventory.py
import log
import common
from ifcgroup import IFCGROUP

from utils import *

class IFCINVENTORY(IFCGROUP):
    """"""
    def __init__(self,id,arg):
        super(IFCINVENTORY,self).__init__(id,arg)
        self.type='IFCINVENTORY'
        self.inverse={}
        self.InventoryType=None #IfcInventoryTypeEnum
        self.Jurisdiction=None #IfcActorSelect
        self.ResponsiblePersons=None #SET
        self.LastUpdateDate=None #IfcCalendarDate
        self.CurrentValue=None #IfcCostValue
        self.OriginalValue=None #IfcCostValue


    def load(self):
        """register inverses"""
        if not super(IFCINVENTORY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCINVENTORY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InventoryType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Jurisdiction= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ResponsiblePersons= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LastUpdateDate= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CurrentValue= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OriginalValue= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCINVENTORY,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCINVENTORY,self).toString()       
        line += typerefToSPF(self.InventoryType)+','
        line += typerefToSPF(self.Jurisdiction)+','
        line += listParamToSPF(self.ResponsiblePersons,idToSPF)+','
        line += idToSPF(self.LastUpdateDate)+','
        line += idToSPF(self.CurrentValue)+','
        line += idToSPF(self.OriginalValue)+','

        return line
