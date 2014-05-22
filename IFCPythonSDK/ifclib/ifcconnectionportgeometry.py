#!/usr/bin/python
#coding=utf-8
#Filename:IfcConnectionPortGeometry.py
import log
import common
from ifcconnectiongeometry import IFCCONNECTIONGEOMETRY

from utils import *

class IFCCONNECTIONPORTGEOMETRY(IFCCONNECTIONGEOMETRY):
    """"""
    def __init__(self,id,arg):
        super(IFCCONNECTIONPORTGEOMETRY,self).__init__(id,arg)
        self.type='IFCCONNECTIONPORTGEOMETRY'
        self.inverse={}
        self.LocationAtRelatingElement=None #IfcAxis2Placement
        self.LocationAtRelatedElement=None #IfcAxis2Placement
        self.ProfileOfPort=None #IfcProfileDef


    def load(self):
        """register inverses"""
        if not super(IFCCONNECTIONPORTGEOMETRY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONNECTIONPORTGEOMETRY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LocationAtRelatingElement= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LocationAtRelatedElement= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProfileOfPort= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONNECTIONPORTGEOMETRY,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCCONNECTIONPORTGEOMETRY,self).toString()       
        line += typerefToSPF(self.LocationAtRelatingElement)+','
        line += typerefToSPF(self.LocationAtRelatedElement)+','
        line += idToSPF(self.ProfileOfPort)+','

        return line
