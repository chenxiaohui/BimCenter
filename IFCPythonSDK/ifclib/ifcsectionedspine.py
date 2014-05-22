#!/usr/bin/python
#coding=utf-8
#Filename:IfcSectionedSpine.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCSECTIONEDSPINE(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCSECTIONEDSPINE,self).__init__(id,arg)
        self.type='IFCSECTIONEDSPINE'
        self.inverse={}
        self.SpineCurve=None #IfcCompositeCurve
        self.CrossSections=None #LIST
        self.CrossSectionPositions=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCSECTIONEDSPINE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSECTIONEDSPINE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SpineCurve= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CrossSections= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CrossSectionPositions= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSECTIONEDSPINE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCSECTIONEDSPINE,self).toString()       
        line += idToSPF(self.SpineCurve)+','
        line += listParamToSPF(self.CrossSections,idToSPF)+','
        line += listParamToSPF(self.CrossSectionPositions,idToSPF)+','

        return line
