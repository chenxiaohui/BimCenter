#!/usr/bin/python
#coding=utf-8
#Filename:IfcConnectionSurfaceGeometry.py
import log
import common
from ifcconnectiongeometry import IFCCONNECTIONGEOMETRY

from utils import *

class IFCCONNECTIONSURFACEGEOMETRY(IFCCONNECTIONGEOMETRY):
    """"""
    def __init__(self,id,arg):
        super(IFCCONNECTIONSURFACEGEOMETRY,self).__init__(id,arg)
        self.type='IFCCONNECTIONSURFACEGEOMETRY'
        self.inverse={}
        self.SurfaceOnRelatingElement=None #IfcSurfaceOrFaceSurface
        self.SurfaceOnRelatedElement=None #IfcSurfaceOrFaceSurface


    def load(self):
        """register inverses"""
        if not super(IFCCONNECTIONSURFACEGEOMETRY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONNECTIONSURFACEGEOMETRY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SurfaceOnRelatingElement= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SurfaceOnRelatedElement= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONNECTIONSURFACEGEOMETRY,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCONNECTIONSURFACEGEOMETRY,self).toString()       
        line += typerefToSPF(self.SurfaceOnRelatingElement)+','
        line += typerefToSPF(self.SurfaceOnRelatedElement)+','

        return line
