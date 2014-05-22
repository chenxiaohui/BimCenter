#!/usr/bin/python
#coding=utf-8
#Filename:IfcAnnotationFillArea.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCANNOTATIONFILLAREA(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCANNOTATIONFILLAREA,self).__init__(id,arg)
        self.type='IFCANNOTATIONFILLAREA'
        self.inverse={}
        self.OuterBoundary=None #IfcCurve
        self.InnerBoundaries=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCANNOTATIONFILLAREA,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCANNOTATIONFILLAREA,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OuterBoundary= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InnerBoundaries= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCANNOTATIONFILLAREA,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCANNOTATIONFILLAREA,self).toString()       
        line += idToSPF(self.OuterBoundary)+','
        line += listParamToSPF(self.InnerBoundaries,idToSPF)+','

        return line
