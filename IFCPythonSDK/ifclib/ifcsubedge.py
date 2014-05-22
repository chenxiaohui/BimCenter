#!/usr/bin/python
#coding=utf-8
#Filename:IfcSubedge.py
import log
import common
from ifcedge import IFCEDGE

from utils import *

class IFCSUBEDGE(IFCEDGE):
    """"""
    def __init__(self,id,arg):
        super(IFCSUBEDGE,self).__init__(id,arg)
        self.type='IFCSUBEDGE'
        self.inverse={}
        self.ParentEdge=None #IfcEdge


    def load(self):
        """register inverses"""
        if not super(IFCSUBEDGE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSUBEDGE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ParentEdge= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSUBEDGE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSUBEDGE,self).toString()       
        line += idToSPF(self.ParentEdge)+','

        return line
