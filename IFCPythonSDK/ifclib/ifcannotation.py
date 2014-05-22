#!/usr/bin/python
#coding=utf-8
#Filename:IfcAnnotation.py
import log
import common
from ifcproduct import IFCPRODUCT

from utils import *

class IFCANNOTATION(IFCPRODUCT):
    """"""
    def __init__(self,id,arg):
        super(IFCANNOTATION,self).__init__(id,arg)
        self.type='IFCANNOTATION'
        self.inverse={}
        self.inverse['ContainedInStructure']=[] #inverse:SET of IfcRelContainedInSpatialStructure


    def load(self):
        """register inverses"""
        if not super(IFCANNOTATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCANNOTATION,self).init():
            return False

        inverses = self.args.getInverses('IFCRELCONTAINEDINSPATIALSTRUCTURE', 'RelatedElements');
        if inverses:
            self.inverse['ContainedInStructure']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCANNOTATION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCANNOTATION,self).toString()       

        return line
