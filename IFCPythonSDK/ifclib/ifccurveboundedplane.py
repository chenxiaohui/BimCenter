#!/usr/bin/python
#coding=utf-8
#Filename:IfcCurveBoundedPlane.py
import log
import common
from ifcboundedsurface import IFCBOUNDEDSURFACE

from utils import *

class IFCCURVEBOUNDEDPLANE(IFCBOUNDEDSURFACE):
    """"""
    def __init__(self,id,arg):
        super(IFCCURVEBOUNDEDPLANE,self).__init__(id,arg)
        self.type='IFCCURVEBOUNDEDPLANE'
        self.inverse={}
        self.BasisSurface=None #IfcPlane
        self.OuterBoundary=None #IfcCurve
        self.InnerBoundaries=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCCURVEBOUNDEDPLANE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCURVEBOUNDEDPLANE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BasisSurface= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OuterBoundary= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InnerBoundaries= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCURVEBOUNDEDPLANE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCCURVEBOUNDEDPLANE,self).toString()       
        line += idToSPF(self.BasisSurface)+','
        line += idToSPF(self.OuterBoundary)+','
        line += listParamToSPF(self.InnerBoundaries,idToSPF)+','

        return line
