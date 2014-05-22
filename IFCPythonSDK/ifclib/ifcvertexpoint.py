#!/usr/bin/python
#coding=utf-8
#Filename:IfcVertexPoint.py
import log
import common
from ifcvertex import IFCVERTEX

from utils import *

class IFCVERTEXPOINT(IFCVERTEX):
    """"""
    def __init__(self,id,arg):
        super(IFCVERTEXPOINT,self).__init__(id,arg)
        self.type='IFCVERTEXPOINT'
        self.inverse={}
        self.VertexGeometry=None #IfcPoint


    def load(self):
        """register inverses"""
        if not super(IFCVERTEXPOINT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCVERTEXPOINT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VertexGeometry= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCVERTEXPOINT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCVERTEXPOINT,self).toString()       
        line += idToSPF(self.VertexGeometry)+','

        return line
