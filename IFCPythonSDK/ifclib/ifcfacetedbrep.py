#!/usr/bin/python
#coding=utf-8
#Filename:IfcFacetedBrep.py
import log
import common
from ifcmanifoldsolidbrep import IFCMANIFOLDSOLIDBREP

from utils import *

class IFCFACETEDBREP(IFCMANIFOLDSOLIDBREP):
    """"""
    def __init__(self,id,arg):
        super(IFCFACETEDBREP,self).__init__(id,arg)
        self.type='IFCFACETEDBREP'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFACETEDBREP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFACETEDBREP,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFACETEDBREP,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFACETEDBREP,self).toString()       

        return line
