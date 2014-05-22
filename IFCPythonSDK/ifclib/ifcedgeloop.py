#!/usr/bin/python
#coding=utf-8
#Filename:IfcEdgeLoop.py
import log
import common
from ifcloop import IFCLOOP

from utils import *

class IFCEDGELOOP(IFCLOOP):
    """"""
    def __init__(self,id,arg):
        super(IFCEDGELOOP,self).__init__(id,arg)
        self.type='IFCEDGELOOP'
        self.inverse={}
        self.EdgeList=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCEDGELOOP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEDGELOOP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EdgeList= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEDGELOOP,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCEDGELOOP,self).toString()       
        line += listParamToSPF(self.EdgeList,idToSPF)+','

        return line
