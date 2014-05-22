#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralSurfaceMemberVarying.py
import log
import common
from ifcstructuralsurfacemember import IFCSTRUCTURALSURFACEMEMBER

from utils import *

class IFCSTRUCTURALSURFACEMEMBERVARYING(IFCSTRUCTURALSURFACEMEMBER):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALSURFACEMEMBERVARYING,self).__init__(id,arg)
        self.type='IFCSTRUCTURALSURFACEMEMBERVARYING'
        self.inverse={}
        self.SubsequentThickness=None #LIST
        self.VaryingThicknessLocation=None #IfcShapeAspect


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALSURFACEMEMBERVARYING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALSURFACEMEMBERVARYING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SubsequentThickness= getIdListParam(arg,spfToInteger)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VaryingThicknessLocation= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALSURFACEMEMBERVARYING,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALSURFACEMEMBERVARYING,self).toString()       
        line += listParamToSPF(self.SubsequentThickness,integerToSPF)+','
        line += idToSPF(self.VaryingThicknessLocation)+','

        return line
