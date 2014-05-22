#!/usr/bin/python
#coding=utf-8
#Filename:IfcSpace.py
import log
import common
from ifcspatialstructureelement import IFCSPATIALSTRUCTUREELEMENT

from utils import *

class IFCSPACE(IFCSPATIALSTRUCTUREELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCSPACE,self).__init__(id,arg)
        self.type='IFCSPACE'
        self.inverse={}
        self.InteriorOrExteriorSpace=None #IfcInternalOrExternalEnum
        self.ElevationWithFlooring=None #IfcLengthMeasure
        self.inverse['BoundedBy']=[] #inverse:SET of IfcRelSpaceBoundary
        self.inverse['HasCoverings']=[] #inverse:SET of IfcRelCoversSpaces


    def load(self):
        """register inverses"""
        if not super(IFCSPACE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSPACE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InteriorOrExteriorSpace= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ElevationWithFlooring= spfToInteger(arg)

        inverses = self.args.getInverses('IFCRELSPACEBOUNDARY', 'RelatingSpace');
        if inverses:
            self.inverse['BoundedBy']=inverses

        inverses = self.args.getInverses('IFCRELCOVERSSPACES', 'RelatedSpace');
        if inverses:
            self.inverse['HasCoverings']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSPACE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSPACE,self).toString()       
        line += typerefToSPF(self.InteriorOrExteriorSpace)+','
        line += integerToSPF(self.ElevationWithFlooring)+','

        return line
