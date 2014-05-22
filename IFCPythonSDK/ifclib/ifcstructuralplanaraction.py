#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralPlanarAction.py
import log
import common
from ifcstructuralaction import IFCSTRUCTURALACTION

from utils import *

class IFCSTRUCTURALPLANARACTION(IFCSTRUCTURALACTION):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALPLANARACTION,self).__init__(id,arg)
        self.type='IFCSTRUCTURALPLANARACTION'
        self.inverse={}
        self.ProjectedOrTrue=None #IfcProjectedOrTrueLengthEnum


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALPLANARACTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALPLANARACTION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProjectedOrTrue= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALPLANARACTION,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALPLANARACTION,self).toString()       
        line += typerefToSPF(self.ProjectedOrTrue)+','

        return line
