#!/usr/bin/python
#coding=utf-8
#Filename:IfcConstructionMaterialResource.py
import log
import common
from ifcconstructionresource import IFCCONSTRUCTIONRESOURCE

from utils import *

class IFCCONSTRUCTIONMATERIALRESOURCE(IFCCONSTRUCTIONRESOURCE):
    """"""
    def __init__(self,id,arg):
        super(IFCCONSTRUCTIONMATERIALRESOURCE,self).__init__(id,arg)
        self.type='IFCCONSTRUCTIONMATERIALRESOURCE'
        self.inverse={}
        self.Suppliers=None #SET
        self.UsageRatio=None #IfcRatioMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCONSTRUCTIONMATERIALRESOURCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONSTRUCTIONMATERIALRESOURCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Suppliers= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UsageRatio= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONSTRUCTIONMATERIALRESOURCE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCONSTRUCTIONMATERIALRESOURCE,self).toString()       
        line += listParamToSPF(self.Suppliers,typerefToSPF)+','
        line += integerToSPF(self.UsageRatio)+','

        return line
