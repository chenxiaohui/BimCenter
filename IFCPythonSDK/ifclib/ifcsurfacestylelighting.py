#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceStyleLighting.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCSURFACESTYLELIGHTING(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCSURFACESTYLELIGHTING,self).__init__(id,arg)
        self.type='IFCSURFACESTYLELIGHTING'
        self.inverse={}
        self.DiffuseTransmissionColour=None #IfcColourRgb
        self.DiffuseReflectionColour=None #IfcColourRgb
        self.TransmissionColour=None #IfcColourRgb
        self.ReflectanceColour=None #IfcColourRgb


    def load(self):
        """register inverses"""
        if not super(IFCSURFACESTYLELIGHTING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSURFACESTYLELIGHTING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DiffuseTransmissionColour= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DiffuseReflectionColour= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TransmissionColour= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ReflectanceColour= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSURFACESTYLELIGHTING,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCSURFACESTYLELIGHTING,self).toString()       
        line += idToSPF(self.DiffuseTransmissionColour)+','
        line += idToSPF(self.DiffuseReflectionColour)+','
        line += idToSPF(self.TransmissionColour)+','
        line += idToSPF(self.ReflectanceColour)+','

        return line
