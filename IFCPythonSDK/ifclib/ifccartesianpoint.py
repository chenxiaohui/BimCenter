#!/usr/bin/python
#coding=utf-8
#Filename:IfcCartesianPoint.py
import log
import common
from ifcpoint import IFCPOINT

from utils import *

class IFCCARTESIANPOINT(IFCPOINT):
    """"""
    def __init__(self,id,arg):
        super(IFCCARTESIANPOINT,self).__init__(id,arg)
        self.type='IFCCARTESIANPOINT'
        self.inverse={}
        self.Coordinates=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCCARTESIANPOINT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCARTESIANPOINT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Coordinates= getIdListParam(arg,spfToInteger)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCARTESIANPOINT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCARTESIANPOINT,self).toString()       
        line += listParamToSPF(self.Coordinates,integerToSPF)+','

        return line
