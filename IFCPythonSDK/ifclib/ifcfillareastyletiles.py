#!/usr/bin/python
#coding=utf-8
#Filename:IfcFillAreaStyleTiles.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCFILLAREASTYLETILES(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCFILLAREASTYLETILES,self).__init__(id,arg)
        self.type='IFCFILLAREASTYLETILES'
        self.inverse={}
        self.TilingPattern=None #IfcOneDirectionRepeatFactor
        self.Tiles=None #SET
        self.TilingScale=None #IfcPositiveRatioMeasure


    def load(self):
        """register inverses"""
        if not super(IFCFILLAREASTYLETILES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFILLAREASTYLETILES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TilingPattern= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Tiles= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TilingScale= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFILLAREASTYLETILES,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCFILLAREASTYLETILES,self).toString()       
        line += idToSPF(self.TilingPattern)+','
        line += listParamToSPF(self.Tiles,typerefToSPF)+','
        line += integerToSPF(self.TilingScale)+','

        return line
