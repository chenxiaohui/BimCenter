#!/usr/bin/python
#coding=utf-8
#Filename:IfcEdge.py
import log
import common
from ifctopologicalrepresentationitem import IFCTOPOLOGICALREPRESENTATIONITEM

from utils import *

class IFCEDGE(IFCTOPOLOGICALREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCEDGE,self).__init__(id,arg)
        self.type='IFCEDGE'
        self.inverse={}
        self.EdgeStart=None #IfcVertex
        self.EdgeEnd=None #IfcVertex


    def load(self):
        """register inverses"""
        if not super(IFCEDGE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEDGE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EdgeStart= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EdgeEnd= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEDGE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCEDGE,self).toString()       
        line += idToSPF(self.EdgeStart)+','
        line += idToSPF(self.EdgeEnd)+','

        return line
