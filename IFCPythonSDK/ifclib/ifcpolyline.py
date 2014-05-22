#!/usr/bin/python
#coding=utf-8
#Filename:IfcPolyline.py
import log
import common
from ifcboundedcurve import IFCBOUNDEDCURVE

from utils import *

class IFCPOLYLINE(IFCBOUNDEDCURVE):
    """"""
    def __init__(self,id,arg):
        super(IFCPOLYLINE,self).__init__(id,arg)
        self.type='IFCPOLYLINE'
        self.inverse={}
        self.Points=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCPOLYLINE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPOLYLINE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Points= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPOLYLINE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPOLYLINE,self).toString()       
        line += listParamToSPF(self.Points,idToSPF)+','

        return line
