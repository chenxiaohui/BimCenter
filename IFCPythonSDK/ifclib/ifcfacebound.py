#!/usr/bin/python
#coding=utf-8
#Filename:IfcFaceBound.py
import log
import common
from ifctopologicalrepresentationitem import IFCTOPOLOGICALREPRESENTATIONITEM

from utils import *

class IFCFACEBOUND(IFCTOPOLOGICALREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCFACEBOUND,self).__init__(id,arg)
        self.type='IFCFACEBOUND'
        self.inverse={}
        self.Bound=None #IfcLoop
        self.Orientation=None #BOOLEAN


    def load(self):
        """register inverses"""
        if not super(IFCFACEBOUND,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFACEBOUND,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Bound= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Orientation= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFACEBOUND,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCFACEBOUND,self).toString()       
        line += idToSPF(self.Bound)+','
        line += logicalToSPF(self.Orientation)+','

        return line
