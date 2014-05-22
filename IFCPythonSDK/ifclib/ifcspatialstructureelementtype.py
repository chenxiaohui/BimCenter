#!/usr/bin/python
#coding=utf-8
#Filename:IfcSpatialStructureElementType.py
import log
import common
from ifcelementtype import IFCELEMENTTYPE

from utils import *

class IFCSPATIALSTRUCTUREELEMENTTYPE(IFCELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCSPATIALSTRUCTUREELEMENTTYPE,self).__init__(id,arg)
        self.type='IFCSPATIALSTRUCTUREELEMENTTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSPATIALSTRUCTUREELEMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSPATIALSTRUCTUREELEMENTTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSPATIALSTRUCTUREELEMENTTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSPATIALSTRUCTUREELEMENTTYPE,self).toString()       

        return line
