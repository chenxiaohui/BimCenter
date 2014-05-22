#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceOfLinearExtrusion.py
import log
import common
from ifcsweptsurface import IFCSWEPTSURFACE

from utils import *

class IFCSURFACEOFLINEAREXTRUSION(IFCSWEPTSURFACE):
    """"""
    def __init__(self,id,arg):
        super(IFCSURFACEOFLINEAREXTRUSION,self).__init__(id,arg)
        self.type='IFCSURFACEOFLINEAREXTRUSION'
        self.inverse={}
        self.ExtrudedDirection=None #IfcDirection
        self.Depth=None #IfcLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSURFACEOFLINEAREXTRUSION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSURFACEOFLINEAREXTRUSION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ExtrudedDirection= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Depth= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSURFACEOFLINEAREXTRUSION,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSURFACEOFLINEAREXTRUSION,self).toString()       
        line += idToSPF(self.ExtrudedDirection)+','
        line += integerToSPF(self.Depth)+','

        return line
