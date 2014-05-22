#!/usr/bin/python
#coding=utf-8
#Filename:IfcClassificationNotation.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCLASSIFICATIONNOTATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCLASSIFICATIONNOTATION,self).__init__(id,arg)
        self.type='IFCCLASSIFICATIONNOTATION'
        self.inverse={}
        self.NotationFacets=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCCLASSIFICATIONNOTATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCLASSIFICATIONNOTATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.NotationFacets= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCLASSIFICATIONNOTATION,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCLASSIFICATIONNOTATION,self).toString()       
        line += listParamToSPF(self.NotationFacets,idToSPF)+','

        return line
