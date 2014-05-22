#!/usr/bin/python
#coding=utf-8
#Filename:IfcMaterialLayer.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCMATERIALLAYER(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCMATERIALLAYER,self).__init__(id,arg)
        self.type='IFCMATERIALLAYER'
        self.inverse={}
        self.Material=None #IfcMaterial
        self.LayerThickness=None #IfcPositiveLengthMeasure
        self.IsVentilated=None #IfcLogical
        self.inverse['ToMaterialLayerSet']=[] #inverse:IfcMaterialLayerSet of Alone


    def load(self):
        """register inverses"""
        if not super(IFCMATERIALLAYER,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMATERIALLAYER,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Material= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LayerThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.IsVentilated= spfToLogical(arg)

        inverses = self.args.getInverses('IFCMATERIALLAYERSET', 'MaterialLayers');
        if inverses:
            self.inverse['ToMaterialLayerSet']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMATERIALLAYER,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCMATERIALLAYER,self).toString()       
        line += idToSPF(self.Material)+','
        line += integerToSPF(self.LayerThickness)+','
        line += logicalToSPF(self.IsVentilated)+','

        return line
