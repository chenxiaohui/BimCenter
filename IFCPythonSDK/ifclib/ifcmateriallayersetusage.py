#!/usr/bin/python
#coding=utf-8
#Filename:IfcMaterialLayerSetUsage.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCMATERIALLAYERSETUSAGE(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCMATERIALLAYERSETUSAGE,self).__init__(id,arg)
        self.type='IFCMATERIALLAYERSETUSAGE'
        self.inverse={}
        self.ForLayerSet=None #IfcMaterialLayerSet
        self.LayerSetDirection=None #IfcLayerSetDirectionEnum
        self.DirectionSense=None #IfcDirectionSenseEnum
        self.OffsetFromReferenceLine=None #IfcLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCMATERIALLAYERSETUSAGE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMATERIALLAYERSETUSAGE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ForLayerSet= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LayerSetDirection= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DirectionSense= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OffsetFromReferenceLine= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMATERIALLAYERSETUSAGE,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCMATERIALLAYERSETUSAGE,self).toString()       
        line += idToSPF(self.ForLayerSet)+','
        line += typerefToSPF(self.LayerSetDirection)+','
        line += typerefToSPF(self.DirectionSense)+','
        line += integerToSPF(self.OffsetFromReferenceLine)+','

        return line
