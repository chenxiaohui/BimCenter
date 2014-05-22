#!/usr/bin/python
#coding=utf-8
#Filename:IfcManifoldSolidBrep.py
import log
import common
from ifcsolidmodel import IFCSOLIDMODEL

from utils import *

class IFCMANIFOLDSOLIDBREP(IFCSOLIDMODEL):
    """"""
    def __init__(self,id,arg):
        super(IFCMANIFOLDSOLIDBREP,self).__init__(id,arg)
        self.type='IFCMANIFOLDSOLIDBREP'
        self.inverse={}
        self.Outer=None #IfcClosedShell


    def load(self):
        """register inverses"""
        if not super(IFCMANIFOLDSOLIDBREP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMANIFOLDSOLIDBREP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Outer= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMANIFOLDSOLIDBREP,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCMANIFOLDSOLIDBREP,self).toString()       
        line += idToSPF(self.Outer)+','

        return line
