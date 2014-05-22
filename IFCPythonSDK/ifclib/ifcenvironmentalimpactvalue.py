#!/usr/bin/python
#coding=utf-8
#Filename:IfcEnvironmentalImpactValue.py
import log
import common
from ifcappliedvalue import IFCAPPLIEDVALUE

from utils import *

class IFCENVIRONMENTALIMPACTVALUE(IFCAPPLIEDVALUE):
    """"""
    def __init__(self,id,arg):
        super(IFCENVIRONMENTALIMPACTVALUE,self).__init__(id,arg)
        self.type='IFCENVIRONMENTALIMPACTVALUE'
        self.inverse={}
        self.ImpactType=None #IfcLabel
        self.Category=None #IfcEnvironmentalImpactCategoryEnum
        self.UserDefinedCategory=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCENVIRONMENTALIMPACTVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCENVIRONMENTALIMPACTVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ImpactType= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Category= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedCategory= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCENVIRONMENTALIMPACTVALUE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCENVIRONMENTALIMPACTVALUE,self).toString()       
        line += strToSPF(self.ImpactType)+','
        line += typerefToSPF(self.Category)+','
        line += strToSPF(self.UserDefinedCategory)+','

        return line
