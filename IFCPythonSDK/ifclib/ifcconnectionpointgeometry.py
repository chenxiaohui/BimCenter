#!/usr/bin/python
#coding=utf-8
#Filename:IfcConnectionPointGeometry.py
import log
import common
from ifcconnectiongeometry import IFCCONNECTIONGEOMETRY

from utils import *

class IFCCONNECTIONPOINTGEOMETRY(IFCCONNECTIONGEOMETRY):
    """"""
    def __init__(self,id,arg):
        super(IFCCONNECTIONPOINTGEOMETRY,self).__init__(id,arg)
        self.type='IFCCONNECTIONPOINTGEOMETRY'
        self.inverse={}
        self.PointOnRelatingElement=None #IfcPointOrVertexPoint
        self.PointOnRelatedElement=None #IfcPointOrVertexPoint


    def load(self):
        """register inverses"""
        if not super(IFCCONNECTIONPOINTGEOMETRY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONNECTIONPOINTGEOMETRY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PointOnRelatingElement= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PointOnRelatedElement= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONNECTIONPOINTGEOMETRY,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCONNECTIONPOINTGEOMETRY,self).toString()       
        line += typerefToSPF(self.PointOnRelatingElement)+','
        line += typerefToSPF(self.PointOnRelatedElement)+','

        return line
