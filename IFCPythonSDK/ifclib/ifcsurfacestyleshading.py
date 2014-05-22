#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceStyleShading.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCSURFACESTYLESHADING(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCSURFACESTYLESHADING,self).__init__(id,arg)
        self.type='IFCSURFACESTYLESHADING'
        self.inverse={}
        self.SurfaceColour=None #IfcColourRgb


    def load(self):
        """register inverses"""
        if not super(IFCSURFACESTYLESHADING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSURFACESTYLESHADING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SurfaceColour= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSURFACESTYLESHADING,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSURFACESTYLESHADING,self).toString()       
        line += idToSPF(self.SurfaceColour)+','

        return line
