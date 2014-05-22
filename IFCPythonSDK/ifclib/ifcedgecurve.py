#!/usr/bin/python
#coding=utf-8
#Filename:IfcEdgeCurve.py
import log
import common
from ifcedge import IFCEDGE

from utils import *

class IFCEDGECURVE(IFCEDGE):
    """"""
    def __init__(self,id,arg):
        super(IFCEDGECURVE,self).__init__(id,arg)
        self.type='IFCEDGECURVE'
        self.inverse={}
        self.EdgeGeometry=None #IfcCurve
        self.SameSense=None #BOOLEAN


    def load(self):
        """register inverses"""
        if not super(IFCEDGECURVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEDGECURVE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EdgeGeometry= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SameSense= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEDGECURVE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCEDGECURVE,self).toString()       
        line += idToSPF(self.EdgeGeometry)+','
        line += logicalToSPF(self.SameSense)+','

        return line
