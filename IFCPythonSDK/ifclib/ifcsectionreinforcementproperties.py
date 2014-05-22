#!/usr/bin/python
#coding=utf-8
#Filename:IfcSectionReinforcementProperties.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCSECTIONREINFORCEMENTPROPERTIES(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCSECTIONREINFORCEMENTPROPERTIES,self).__init__(id,arg)
        self.type='IFCSECTIONREINFORCEMENTPROPERTIES'
        self.inverse={}
        self.LongitudinalStartPosition=None #IfcLengthMeasure
        self.LongitudinalEndPosition=None #IfcLengthMeasure
        self.TransversePosition=None #IfcLengthMeasure
        self.ReinforcementRole=None #IfcReinforcingBarRoleEnum
        self.SectionDefinition=None #IfcSectionProperties
        self.CrossSectionReinforcementDefinitions=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCSECTIONREINFORCEMENTPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSECTIONREINFORCEMENTPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LongitudinalStartPosition= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LongitudinalEndPosition= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TransversePosition= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ReinforcementRole= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SectionDefinition= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CrossSectionReinforcementDefinitions= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSECTIONREINFORCEMENTPROPERTIES,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCSECTIONREINFORCEMENTPROPERTIES,self).toString()       
        line += integerToSPF(self.LongitudinalStartPosition)+','
        line += integerToSPF(self.LongitudinalEndPosition)+','
        line += integerToSPF(self.TransversePosition)+','
        line += typerefToSPF(self.ReinforcementRole)+','
        line += idToSPF(self.SectionDefinition)+','
        line += listParamToSPF(self.CrossSectionReinforcementDefinitions,idToSPF)+','

        return line
