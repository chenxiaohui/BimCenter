#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceCurveSweptAreaSolid.py
import log
import common
from ifcsweptareasolid import IFCSWEPTAREASOLID

from utils import *

class IFCSURFACECURVESWEPTAREASOLID(IFCSWEPTAREASOLID):
    """"""
    def __init__(self,id,arg):
        super(IFCSURFACECURVESWEPTAREASOLID,self).__init__(id,arg)
        self.type='IFCSURFACECURVESWEPTAREASOLID'
        self.inverse={}
        self.Directrix=None #IfcCurve
        self.StartParam=None #IfcParameterValue
        self.EndParam=None #IfcParameterValue
        self.ReferenceSurface=None #IfcSurface


    def load(self):
        """register inverses"""
        if not super(IFCSURFACECURVESWEPTAREASOLID,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSURFACECURVESWEPTAREASOLID,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Directrix= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.StartParam= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EndParam= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ReferenceSurface= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSURFACECURVESWEPTAREASOLID,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCSURFACECURVESWEPTAREASOLID,self).toString()       
        line += idToSPF(self.Directrix)+','
        line += integerToSPF(self.StartParam)+','
        line += integerToSPF(self.EndParam)+','
        line += idToSPF(self.ReferenceSurface)+','

        return line
