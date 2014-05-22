#!/usr/bin/python
#coding=utf-8
#Filename:IfcCurrencyRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCURRENCYRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCURRENCYRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCCURRENCYRELATIONSHIP'
        self.inverse={}
        self.RelatingMonetaryUnit=None #IfcMonetaryUnit
        self.RelatedMonetaryUnit=None #IfcMonetaryUnit
        self.ExchangeRate=None #IfcPositiveRatioMeasure
        self.RateDateTime=None #IfcDateAndTime
        self.RateSource=None #IfcLibraryInformation


    def load(self):
        """register inverses"""
        if not super(IFCCURRENCYRELATIONSHIP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCURRENCYRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingMonetaryUnit= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedMonetaryUnit= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ExchangeRate= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RateDateTime= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RateSource= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCURRENCYRELATIONSHIP,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCCURRENCYRELATIONSHIP,self).toString()       
        line += idToSPF(self.RelatingMonetaryUnit)+','
        line += idToSPF(self.RelatedMonetaryUnit)+','
        line += integerToSPF(self.ExchangeRate)+','
        line += idToSPF(self.RateDateTime)+','
        line += idToSPF(self.RateSource)+','

        return line
