#!/usr/bin/python
#coding=utf-8
#Filename:IfcPresentationLayerWithStyle.py
import log
import common
from ifcpresentationlayerassignment import IFCPRESENTATIONLAYERASSIGNMENT

from utils import *

class IFCPRESENTATIONLAYERWITHSTYLE(IFCPRESENTATIONLAYERASSIGNMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCPRESENTATIONLAYERWITHSTYLE,self).__init__(id,arg)
        self.type='IFCPRESENTATIONLAYERWITHSTYLE'
        self.inverse={}
        self.LayerOn=None #LOGICAL
        self.LayerFrozen=None #LOGICAL
        self.LayerBlocked=None #LOGICAL
        self.LayerStyles=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCPRESENTATIONLAYERWITHSTYLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPRESENTATIONLAYERWITHSTYLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LayerOn= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LayerFrozen= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LayerBlocked= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LayerStyles= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPRESENTATIONLAYERWITHSTYLE,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCPRESENTATIONLAYERWITHSTYLE,self).toString()       
        line += logicalToSPF(self.LayerOn)+','
        line += logicalToSPF(self.LayerFrozen)+','
        line += logicalToSPF(self.LayerBlocked)+','
        line += listParamToSPF(self.LayerStyles,typerefToSPF)+','

        return line
