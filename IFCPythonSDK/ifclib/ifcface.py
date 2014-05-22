#!/usr/bin/python
#coding=utf-8
#Filename:IfcFace.py
import log
import common
from ifctopologicalrepresentationitem import IFCTOPOLOGICALREPRESENTATIONITEM

from utils import *

class IFCFACE(IFCTOPOLOGICALREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCFACE,self).__init__(id,arg)
        self.type='IFCFACE'
        self.inverse={}
        self.Bounds=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCFACE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFACE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Bounds= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFACE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFACE,self).toString()       
        line += listParamToSPF(self.Bounds,idToSPF)+','

        return line
