#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceStyle.py
import log
import common
from ifcpresentationstyle import IFCPRESENTATIONSTYLE

from utils import *

class IFCSURFACESTYLE(IFCPRESENTATIONSTYLE):
    """"""
    def __init__(self,id,arg):
        super(IFCSURFACESTYLE,self).__init__(id,arg)
        self.type='IFCSURFACESTYLE'
        self.inverse={}
        self.Side=None #IfcSurfaceSide
        self.Styles=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCSURFACESTYLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSURFACESTYLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Side= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Styles= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSURFACESTYLE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSURFACESTYLE,self).toString()       
        line += typerefToSPF(self.Side)+','
        line += listParamToSPF(self.Styles,typerefToSPF)+','

        return line
