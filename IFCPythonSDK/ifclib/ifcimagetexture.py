#!/usr/bin/python
#coding=utf-8
#Filename:IfcImageTexture.py
import log
import common
from ifcsurfacetexture import IFCSURFACETEXTURE

from utils import *

class IFCIMAGETEXTURE(IFCSURFACETEXTURE):
    """"""
    def __init__(self,id,arg):
        super(IFCIMAGETEXTURE,self).__init__(id,arg)
        self.type='IFCIMAGETEXTURE'
        self.inverse={}
        self.UrlReference=None #IfcIdentifier


    def load(self):
        """register inverses"""
        if not super(IFCIMAGETEXTURE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCIMAGETEXTURE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UrlReference= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCIMAGETEXTURE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCIMAGETEXTURE,self).toString()       
        line += strToSPF(self.UrlReference)+','

        return line
