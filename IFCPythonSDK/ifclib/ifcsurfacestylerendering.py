#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceStyleRendering.py
import log
import common
from ifcsurfacestyleshading import IFCSURFACESTYLESHADING

from utils import *

class IFCSURFACESTYLERENDERING(IFCSURFACESTYLESHADING):
    """"""
    def __init__(self,id,arg):
        super(IFCSURFACESTYLERENDERING,self).__init__(id,arg)
        self.type='IFCSURFACESTYLERENDERING'
        self.inverse={}
        self.Transparency=None #IfcNormalisedRatioMeasure
        self.DiffuseColour=None #IfcColourOrFactor
        self.TransmissionColour=None #IfcColourOrFactor
        self.DiffuseTransmissionColour=None #IfcColourOrFactor
        self.ReflectionColour=None #IfcColourOrFactor
        self.SpecularColour=None #IfcColourOrFactor
        self.SpecularHighlight=None #IfcSpecularHighlightSelect
        self.ReflectanceMethod=None #IfcReflectanceMethodEnum


    def load(self):
        """register inverses"""
        if not super(IFCSURFACESTYLERENDERING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSURFACESTYLERENDERING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Transparency= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DiffuseColour= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TransmissionColour= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DiffuseTransmissionColour= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ReflectionColour= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SpecularColour= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SpecularHighlight= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ReflectanceMethod= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSURFACESTYLERENDERING,self).getAttrCount()+8

    def toString(self):
        """"""
        line=super(IFCSURFACESTYLERENDERING,self).toString()       
        line += integerToSPF(self.Transparency)+','
        line += typerefToSPF(self.DiffuseColour)+','
        line += typerefToSPF(self.TransmissionColour)+','
        line += typerefToSPF(self.DiffuseTransmissionColour)+','
        line += typerefToSPF(self.ReflectionColour)+','
        line += typerefToSPF(self.SpecularColour)+','
        line += typerefToSPF(self.SpecularHighlight)+','
        line += typerefToSPF(self.ReflectanceMethod)+','

        return line
