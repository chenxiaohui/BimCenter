#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextLiteralWithExtent.py
import log
import common
from ifctextliteral import IFCTEXTLITERAL

from utils import *

class IFCTEXTLITERALWITHEXTENT(IFCTEXTLITERAL):
    """"""
    def __init__(self,id,arg):
        super(IFCTEXTLITERALWITHEXTENT,self).__init__(id,arg)
        self.type='IFCTEXTLITERALWITHEXTENT'
        self.inverse={}
        self.Extent=None #IfcPlanarExtent
        self.BoxAlignment=None #IfcBoxAlignment


    def load(self):
        """register inverses"""
        if not super(IFCTEXTLITERALWITHEXTENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTEXTLITERALWITHEXTENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Extent= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BoxAlignment= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTEXTLITERALWITHEXTENT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCTEXTLITERALWITHEXTENT,self).toString()       
        line += idToSPF(self.Extent)+','
        line += strToSPF(self.BoxAlignment)+','

        return line
