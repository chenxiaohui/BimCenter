#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralSurfaceMember.py
import log
import common
from ifcstructuralmember import IFCSTRUCTURALMEMBER

from utils import *

class IFCSTRUCTURALSURFACEMEMBER(IFCSTRUCTURALMEMBER):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALSURFACEMEMBER,self).__init__(id,arg)
        self.type='IFCSTRUCTURALSURFACEMEMBER'
        self.inverse={}
        self.PredefinedType=None #IfcStructuralSurfaceTypeEnum
        self.Thickness=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALSURFACEMEMBER,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALSURFACEMEMBER,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Thickness= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALSURFACEMEMBER,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALSURFACEMEMBER,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','
        line += integerToSPF(self.Thickness)+','

        return line
