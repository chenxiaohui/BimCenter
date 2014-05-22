#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralCurveMember.py
import log
import common
from ifcstructuralmember import IFCSTRUCTURALMEMBER

from utils import *

class IFCSTRUCTURALCURVEMEMBER(IFCSTRUCTURALMEMBER):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALCURVEMEMBER,self).__init__(id,arg)
        self.type='IFCSTRUCTURALCURVEMEMBER'
        self.inverse={}
        self.PredefinedType=None #IfcStructuralCurveTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALCURVEMEMBER,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALCURVEMEMBER,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALCURVEMEMBER,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALCURVEMEMBER,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
