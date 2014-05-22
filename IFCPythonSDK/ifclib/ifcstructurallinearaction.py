#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLinearAction.py
import log
import common
from ifcstructuralaction import IFCSTRUCTURALACTION

from utils import *

class IFCSTRUCTURALLINEARACTION(IFCSTRUCTURALACTION):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLINEARACTION,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLINEARACTION'
        self.inverse={}
        self.ProjectedOrTrue=None #IfcProjectedOrTrueLengthEnum


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLINEARACTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLINEARACTION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProjectedOrTrue= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALLINEARACTION,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLINEARACTION,self).toString()       
        line += typerefToSPF(self.ProjectedOrTrue)+','

        return line
