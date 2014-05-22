#!/usr/bin/python
#coding=utf-8
#Filename:IfcLine.py
import log
import common
from ifccurve import IFCCURVE

from utils import *

class IFCLINE(IFCCURVE):
    """"""
    def __init__(self,id,arg):
        super(IFCLINE,self).__init__(id,arg)
        self.type='IFCLINE'
        self.inverse={}
        self.Pnt=None #IfcCartesianPoint
        self.Dir=None #IfcVector


    def load(self):
        """register inverses"""
        if not super(IFCLINE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLINE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Pnt= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Dir= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLINE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCLINE,self).toString()       
        line += idToSPF(self.Pnt)+','
        line += idToSPF(self.Dir)+','

        return line
