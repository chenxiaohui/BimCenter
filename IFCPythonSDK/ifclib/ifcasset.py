#!/usr/bin/python
#coding=utf-8
#Filename:IfcAsset.py
import log
import common
from ifcgroup import IFCGROUP

from utils import *

class IFCASSET(IFCGROUP):
    """"""
    def __init__(self,id,arg):
        super(IFCASSET,self).__init__(id,arg)
        self.type='IFCASSET'
        self.inverse={}
        self.AssetID=None #IfcIdentifier
        self.OriginalValue=None #IfcCostValue
        self.CurrentValue=None #IfcCostValue
        self.TotalReplacementCost=None #IfcCostValue
        self.Owner=None #IfcActorSelect
        self.User=None #IfcActorSelect
        self.ResponsiblePerson=None #IfcPerson
        self.IncorporationDate=None #IfcCalendarDate
        self.DepreciatedValue=None #IfcCostValue


    def load(self):
        """register inverses"""
        if not super(IFCASSET,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCASSET,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AssetID= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OriginalValue= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CurrentValue= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TotalReplacementCost= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Owner= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.User= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ResponsiblePerson= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.IncorporationDate= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DepreciatedValue= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCASSET,self).getAttrCount()+9

    def toString(self):
        """"""
        line=super(IFCASSET,self).toString()       
        line += strToSPF(self.AssetID)+','
        line += idToSPF(self.OriginalValue)+','
        line += idToSPF(self.CurrentValue)+','
        line += idToSPF(self.TotalReplacementCost)+','
        line += typerefToSPF(self.Owner)+','
        line += typerefToSPF(self.User)+','
        line += idToSPF(self.ResponsiblePerson)+','
        line += idToSPF(self.IncorporationDate)+','
        line += idToSPF(self.DepreciatedValue)+','

        return line
