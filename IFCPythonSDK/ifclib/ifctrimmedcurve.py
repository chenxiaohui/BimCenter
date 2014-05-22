#!/usr/bin/python
#coding=utf-8
#Filename:IfcTrimmedCurve.py
import log
import common
from ifcboundedcurve import IFCBOUNDEDCURVE

from utils import *

class IFCTRIMMEDCURVE(IFCBOUNDEDCURVE):
    """"""
    def __init__(self,id,arg):
        super(IFCTRIMMEDCURVE,self).__init__(id,arg)
        self.type='IFCTRIMMEDCURVE'
        self.inverse={}
        self.BasisCurve=None #IfcCurve
        self.Trim1=None #SET
        self.Trim2=None #SET
        self.SenseAgreement=None #BOOLEAN
        self.MasterRepresentation=None #IfcTrimmingPreference


    def load(self):
        """register inverses"""
        if not super(IFCTRIMMEDCURVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTRIMMEDCURVE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BasisCurve= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Trim1= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Trim2= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SenseAgreement= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MasterRepresentation= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTRIMMEDCURVE,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCTRIMMEDCURVE,self).toString()       
        line += idToSPF(self.BasisCurve)+','
        line += listParamToSPF(self.Trim1,typerefToSPF)+','
        line += listParamToSPF(self.Trim2,typerefToSPF)+','
        line += logicalToSPF(self.SenseAgreement)+','
        line += typerefToSPF(self.MasterRepresentation)+','

        return line
