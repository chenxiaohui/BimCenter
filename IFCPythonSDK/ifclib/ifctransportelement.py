#!/usr/bin/python
#coding=utf-8
#Filename:IfcTransportElement.py
import log
import common
from ifcelement import IFCELEMENT

from utils import *

class IFCTRANSPORTELEMENT(IFCELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCTRANSPORTELEMENT,self).__init__(id,arg)
        self.type='IFCTRANSPORTELEMENT'
        self.inverse={}
        self.OperationType=None #IfcTransportElementTypeEnum
        self.CapacityByWeight=None #IfcMassMeasure
        self.CapacityByNumber=None #IfcCountMeasure


    def load(self):
        """register inverses"""
        if not super(IFCTRANSPORTELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTRANSPORTELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OperationType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CapacityByWeight= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CapacityByNumber= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTRANSPORTELEMENT,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCTRANSPORTELEMENT,self).toString()       
        line += typerefToSPF(self.OperationType)+','
        line += integerToSPF(self.CapacityByWeight)+','
        line += integerToSPF(self.CapacityByNumber)+','

        return line
