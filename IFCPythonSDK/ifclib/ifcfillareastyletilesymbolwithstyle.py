#!/usr/bin/python
#coding=utf-8
#Filename:IfcFillAreaStyleTileSymbolWithStyle.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCFILLAREASTYLETILESYMBOLWITHSTYLE(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCFILLAREASTYLETILESYMBOLWITHSTYLE,self).__init__(id,arg)
        self.type='IFCFILLAREASTYLETILESYMBOLWITHSTYLE'
        self.inverse={}
        self.Symbol=None #IfcAnnotationSymbolOccurrence


    def load(self):
        """register inverses"""
        if not super(IFCFILLAREASTYLETILESYMBOLWITHSTYLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFILLAREASTYLETILESYMBOLWITHSTYLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Symbol= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFILLAREASTYLETILESYMBOLWITHSTYLE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFILLAREASTYLETILESYMBOLWITHSTYLE,self).toString()       
        line += idToSPF(self.Symbol)+','

        return line
