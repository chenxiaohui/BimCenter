#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceTexture.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCSURFACETEXTURE(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCSURFACETEXTURE,self).__init__(id,arg)
        self.type='IFCSURFACETEXTURE'
        self.inverse={}
        self.RepeatS=None #BOOLEAN
        self.RepeatT=None #BOOLEAN
        self.TextureType=None #IfcSurfaceTextureEnum
        self.TextureTransform=None #IfcCartesianTransformationOperator2D


    def load(self):
        """register inverses"""
        if not super(IFCSURFACETEXTURE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSURFACETEXTURE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RepeatS= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RepeatT= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextureType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextureTransform= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSURFACETEXTURE,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCSURFACETEXTURE,self).toString()       
        line += logicalToSPF(self.RepeatS)+','
        line += logicalToSPF(self.RepeatT)+','
        line += typerefToSPF(self.TextureType)+','
        line += idToSPF(self.TextureTransform)+','

        return line
