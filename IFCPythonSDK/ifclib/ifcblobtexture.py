#!/usr/bin/python
#coding=utf-8
#Filename:IfcBlobTexture.py
import log
import common
from ifcsurfacetexture import IFCSURFACETEXTURE

from utils import *

class IFCBLOBTEXTURE(IFCSURFACETEXTURE):
    """"""
    def __init__(self,id,arg):
        super(IFCBLOBTEXTURE,self).__init__(id,arg)
        self.type='IFCBLOBTEXTURE'
        self.inverse={}
        self.RasterFormat=None #IfcIdentifier
        self.RasterCode=None #BOOLEAN


    def load(self):
        """register inverses"""
        if not super(IFCBLOBTEXTURE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBLOBTEXTURE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RasterFormat= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RasterCode= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBLOBTEXTURE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCBLOBTEXTURE,self).toString()       
        line += strToSPF(self.RasterFormat)+','
        line += logicalToSPF(self.RasterCode)+','

        return line
