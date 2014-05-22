#!/usr/bin/python
#coding=utf-8
#Filename:IfcBoxedHalfSpace.py
import log
import common
from ifchalfspacesolid import IFCHALFSPACESOLID

from utils import *

class IFCBOXEDHALFSPACE(IFCHALFSPACESOLID):
    """"""
    def __init__(self,id,arg):
        super(IFCBOXEDHALFSPACE,self).__init__(id,arg)
        self.type='IFCBOXEDHALFSPACE'
        self.inverse={}
        self.Enclosure=None #IfcBoundingBox


    def load(self):
        """register inverses"""
        if not super(IFCBOXEDHALFSPACE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBOXEDHALFSPACE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Enclosure= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBOXEDHALFSPACE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCBOXEDHALFSPACE,self).toString()       
        line += idToSPF(self.Enclosure)+','

        return line
