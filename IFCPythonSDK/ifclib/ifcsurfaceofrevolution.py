#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceOfRevolution.py
import log
import common
from ifcsweptsurface import IFCSWEPTSURFACE

from utils import *

class IFCSURFACEOFREVOLUTION(IFCSWEPTSURFACE):
    """"""
    def __init__(self,id,arg):
        super(IFCSURFACEOFREVOLUTION,self).__init__(id,arg)
        self.type='IFCSURFACEOFREVOLUTION'
        self.inverse={}
        self.AxisPosition=None #IfcAxis1Placement


    def load(self):
        """register inverses"""
        if not super(IFCSURFACEOFREVOLUTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSURFACEOFREVOLUTION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AxisPosition= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSURFACEOFREVOLUTION,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSURFACEOFREVOLUTION,self).toString()       
        line += idToSPF(self.AxisPosition)+','

        return line
