#!/usr/bin/python
#coding=utf-8
#Filename:IfcConnectionCurveGeometry.py
import log
import common
from ifcconnectiongeometry import IFCCONNECTIONGEOMETRY

from utils import *

class IFCCONNECTIONCURVEGEOMETRY(IFCCONNECTIONGEOMETRY):
    """"""
    def __init__(self,id,arg):
        super(IFCCONNECTIONCURVEGEOMETRY,self).__init__(id,arg)
        self.type='IFCCONNECTIONCURVEGEOMETRY'
        self.inverse={}
        self.CurveOnRelatingElement=None #IfcCurveOrEdgeCurve
        self.CurveOnRelatedElement=None #IfcCurveOrEdgeCurve


    def load(self):
        """register inverses"""
        if not super(IFCCONNECTIONCURVEGEOMETRY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONNECTIONCURVEGEOMETRY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CurveOnRelatingElement= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CurveOnRelatedElement= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONNECTIONCURVEGEOMETRY,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCONNECTIONCURVEGEOMETRY,self).toString()       
        line += typerefToSPF(self.CurveOnRelatingElement)+','
        line += typerefToSPF(self.CurveOnRelatedElement)+','

        return line
