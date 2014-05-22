#!/usr/bin/python
#coding=utf-8
#Filename:IfcOrientedEdge.py
import log
import common
from ifcedge import IFCEDGE

from utils import *

class IFCORIENTEDEDGE(IFCEDGE):
    """"""
    def __init__(self,id,arg):
        super(IFCORIENTEDEDGE,self).__init__(id,arg)
        self.type='IFCORIENTEDEDGE'
        self.inverse={}
        self.EdgeElement=None #IfcEdge
        self.Orientation=None #BOOLEAN


    def load(self):
        """register inverses"""
        if not super(IFCORIENTEDEDGE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCORIENTEDEDGE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EdgeElement= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Orientation= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCORIENTEDEDGE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCORIENTEDEDGE,self).toString()       
        line += idToSPF(self.EdgeElement)+','
        line += logicalToSPF(self.Orientation)+','

        return line
