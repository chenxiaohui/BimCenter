#!/usr/bin/python
#coding=utf-8
#Filename:IfcVertexBasedTextureMap.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCVERTEXBASEDTEXTUREMAP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCVERTEXBASEDTEXTUREMAP,self).__init__(id,arg)
        self.type='IFCVERTEXBASEDTEXTUREMAP'
        self.inverse={}
        self.TextureVertices=None #LIST
        self.TexturePoints=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCVERTEXBASEDTEXTUREMAP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCVERTEXBASEDTEXTUREMAP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextureVertices= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TexturePoints= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCVERTEXBASEDTEXTUREMAP,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCVERTEXBASEDTEXTUREMAP,self).toString()       
        line += listParamToSPF(self.TextureVertices,idToSPF)+','
        line += listParamToSPF(self.TexturePoints,idToSPF)+','

        return line
