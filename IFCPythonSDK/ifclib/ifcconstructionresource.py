#!/usr/bin/python
#coding=utf-8
#Filename:IfcConstructionResource.py
import log
import common
from ifcresource import IFCRESOURCE

from utils import *

class IFCCONSTRUCTIONRESOURCE(IFCRESOURCE):
    """"""
    def __init__(self,id,arg):
        super(IFCCONSTRUCTIONRESOURCE,self).__init__(id,arg)
        self.type='IFCCONSTRUCTIONRESOURCE'
        self.inverse={}
        self.ResourceIdentifier=None #IfcIdentifier
        self.ResourceGroup=None #IfcLabel
        self.ResourceConsumption=None #IfcResourceConsumptionEnum
        self.BaseQuantity=None #IfcMeasureWithUnit


    def load(self):
        """register inverses"""
        if not super(IFCCONSTRUCTIONRESOURCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONSTRUCTIONRESOURCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ResourceIdentifier= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ResourceGroup= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ResourceConsumption= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BaseQuantity= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONSTRUCTIONRESOURCE,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCCONSTRUCTIONRESOURCE,self).toString()       
        line += strToSPF(self.ResourceIdentifier)+','
        line += strToSPF(self.ResourceGroup)+','
        line += typerefToSPF(self.ResourceConsumption)+','
        line += idToSPF(self.BaseQuantity)+','

        return line
