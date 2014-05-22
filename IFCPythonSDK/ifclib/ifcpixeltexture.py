#!/usr/bin/python
#coding=utf-8
#Filename:IfcPixelTexture.py
import log
import common
from ifcsurfacetexture import IFCSURFACETEXTURE

from utils import *

class IFCPIXELTEXTURE(IFCSURFACETEXTURE):
    """"""
    def __init__(self,id,arg):
        super(IFCPIXELTEXTURE,self).__init__(id,arg)
        self.type='IFCPIXELTEXTURE'
        self.inverse={}
        self.Width=None #IfcInteger
        self.Height=None #IfcInteger
        self.ColourComponents=None #IfcInteger
        self.Pixel=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCPIXELTEXTURE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPIXELTEXTURE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Width= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Height= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ColourComponents= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Pixel= getIdListParam(arg,spfToBinary)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPIXELTEXTURE,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCPIXELTEXTURE,self).toString()       
        line += integerToSPF(self.Width)+','
        line += integerToSPF(self.Height)+','
        line += integerToSPF(self.ColourComponents)+','
        line += listParamToSPF(self.Pixel,binaryToSPF)+','

        return line
