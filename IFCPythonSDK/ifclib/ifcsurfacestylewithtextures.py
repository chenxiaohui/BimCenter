#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceStyleWithTextures.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCSURFACESTYLEWITHTEXTURES(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCSURFACESTYLEWITHTEXTURES,self).__init__(id,arg)
        self.type='IFCSURFACESTYLEWITHTEXTURES'
        self.inverse={}
        self.Textures=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCSURFACESTYLEWITHTEXTURES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSURFACESTYLEWITHTEXTURES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Textures= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSURFACESTYLEWITHTEXTURES,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSURFACESTYLEWITHTEXTURES,self).toString()       
        line += listParamToSPF(self.Textures,idToSPF)+','

        return line
