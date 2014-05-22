#!/usr/bin/python
#coding=utf-8
#Filename:IfcVertexLoop.py
import log
import common
from ifcloop import IFCLOOP

from utils import *

class IFCVERTEXLOOP(IFCLOOP):
    """"""
    def __init__(self,id,arg):
        super(IFCVERTEXLOOP,self).__init__(id,arg)
        self.type='IFCVERTEXLOOP'
        self.inverse={}
        self.LoopVertex=None #IfcVertex


    def load(self):
        """register inverses"""
        if not super(IFCVERTEXLOOP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCVERTEXLOOP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LoopVertex= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCVERTEXLOOP,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCVERTEXLOOP,self).toString()       
        line += idToSPF(self.LoopVertex)+','

        return line
