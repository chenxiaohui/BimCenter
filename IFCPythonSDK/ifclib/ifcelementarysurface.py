#!/usr/bin/python
#coding=utf-8
#Filename:IfcElementarySurface.py
import log
import common
from ifcsurface import IFCSURFACE

from utils import *

class IFCELEMENTARYSURFACE(IFCSURFACE):
    """"""
    def __init__(self,id,arg):
        super(IFCELEMENTARYSURFACE,self).__init__(id,arg)
        self.type='IFCELEMENTARYSURFACE'
        self.inverse={}
        self.Position=None #IfcAxis2Placement3D


    def load(self):
        """register inverses"""
        if not super(IFCELEMENTARYSURFACE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELEMENTARYSURFACE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Position= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELEMENTARYSURFACE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCELEMENTARYSURFACE,self).toString()       
        line += idToSPF(self.Position)+','

        return line
