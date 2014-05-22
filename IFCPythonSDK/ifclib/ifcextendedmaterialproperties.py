#!/usr/bin/python
#coding=utf-8
#Filename:IfcExtendedMaterialProperties.py
import log
import common
from ifcmaterialproperties import IFCMATERIALPROPERTIES

from utils import *

class IFCEXTENDEDMATERIALPROPERTIES(IFCMATERIALPROPERTIES):
    """"""
    def __init__(self,id,arg):
        super(IFCEXTENDEDMATERIALPROPERTIES,self).__init__(id,arg)
        self.type='IFCEXTENDEDMATERIALPROPERTIES'
        self.inverse={}
        self.ExtendedProperties=None #SET
        self.Description=None #IfcText
        self.Name=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCEXTENDEDMATERIALPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEXTENDEDMATERIALPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ExtendedProperties= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEXTENDEDMATERIALPROPERTIES,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCEXTENDEDMATERIALPROPERTIES,self).toString()       
        line += listParamToSPF(self.ExtendedProperties,idToSPF)+','
        line += strToSPF(self.Description)+','
        line += strToSPF(self.Name)+','

        return line
