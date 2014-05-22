#!/usr/bin/python
#coding=utf-8
#Filename:IfcDirection.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCDIRECTION(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCDIRECTION,self).__init__(id,arg)
        self.type='IFCDIRECTION'
        self.inverse={}
        self.DirectionRatios=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCDIRECTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDIRECTION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DirectionRatios= getIdListParam(arg,spfToInteger)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDIRECTION,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCDIRECTION,self).toString()       
        line += listParamToSPF(self.DirectionRatios,integerToSPF)+','

        return line
