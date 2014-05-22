#!/usr/bin/python
#coding=utf-8
#Filename:IfcIrregularTimeSeries.py
import log
import common
from ifctimeseries import IFCTIMESERIES

from utils import *

class IFCIRREGULARTIMESERIES(IFCTIMESERIES):
    """"""
    def __init__(self,id,arg):
        super(IFCIRREGULARTIMESERIES,self).__init__(id,arg)
        self.type='IFCIRREGULARTIMESERIES'
        self.inverse={}
        self.Values=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCIRREGULARTIMESERIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCIRREGULARTIMESERIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Values= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCIRREGULARTIMESERIES,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCIRREGULARTIMESERIES,self).toString()       
        line += listParamToSPF(self.Values,idToSPF)+','

        return line
