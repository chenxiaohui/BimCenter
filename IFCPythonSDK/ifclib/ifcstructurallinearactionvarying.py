#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLinearActionVarying.py
import log
import common
from ifcstructurallinearaction import IFCSTRUCTURALLINEARACTION

from utils import *

class IFCSTRUCTURALLINEARACTIONVARYING(IFCSTRUCTURALLINEARACTION):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLINEARACTIONVARYING,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLINEARACTIONVARYING'
        self.inverse={}
        self.VaryingAppliedLoadLocation=None #IfcShapeAspect
        self.SubsequentAppliedLoads=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLINEARACTIONVARYING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLINEARACTIONVARYING,self).init():
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
        return super(IFCSTRUCTURALLINEARACTIONVARYING,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLINEARACTIONVARYING,self).toString()       
        line += idToSPF(self.VaryingAppliedLoadLocation)+','
        line += listParamToSPF(self.SubsequentAppliedLoads,idToSPF)+','

        return line
