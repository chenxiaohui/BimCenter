#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceStyleRefraction.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCSURFACESTYLEREFRACTION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCSURFACESTYLEREFRACTION,self).__init__(id,arg)
        self.type='IFCSURFACESTYLEREFRACTION'
        self.inverse={}
        self.RefractionIndex=None #IfcReal
        self.DispersionFactor=None #IfcReal


    def load(self):
        """register inverses"""
        if not super(IFCSURFACESTYLEREFRACTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSURFACESTYLEREFRACTION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RefractionIndex= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DispersionFactor= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSURFACESTYLEREFRACTION,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSURFACESTYLEREFRACTION,self).toString()       
        line += integerToSPF(self.RefractionIndex)+','
        line += integerToSPF(self.DispersionFactor)+','

        return line
