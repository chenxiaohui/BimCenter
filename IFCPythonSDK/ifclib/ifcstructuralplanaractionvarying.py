#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralPlanarActionVarying.py
import log
import common
from ifcstructuralplanaraction import IFCSTRUCTURALPLANARACTION

from utils import *

class IFCSTRUCTURALPLANARACTIONVARYING(IFCSTRUCTURALPLANARACTION):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALPLANARACTIONVARYING,self).__init__(id,arg)
        self.type='IFCSTRUCTURALPLANARACTIONVARYING'
        self.inverse={}
        self.VaryingAppliedLoadLocation=None #IfcShapeAspect
        self.SubsequentAppliedLoads=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALPLANARACTIONVARYING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALPLANARACTIONVARYING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VaryingAppliedLoadLocation= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SubsequentAppliedLoads= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALPLANARACTIONVARYING,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALPLANARACTIONVARYING,self).toString()       
        line += idToSPF(self.VaryingAppliedLoadLocation)+','
        line += listParamToSPF(self.SubsequentAppliedLoads,idToSPF)+','

        return line
