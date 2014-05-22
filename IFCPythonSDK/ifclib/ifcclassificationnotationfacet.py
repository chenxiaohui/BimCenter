#!/usr/bin/python
#coding=utf-8
#Filename:IfcClassificationNotationFacet.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCLASSIFICATIONNOTATIONFACET(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCLASSIFICATIONNOTATIONFACET,self).__init__(id,arg)
        self.type='IFCCLASSIFICATIONNOTATIONFACET'
        self.inverse={}
        self.NotationValue=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCCLASSIFICATIONNOTATIONFACET,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCLASSIFICATIONNOTATIONFACET,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.NotationValue= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCLASSIFICATIONNOTATIONFACET,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCLASSIFICATIONNOTATIONFACET,self).toString()       
        line += strToSPF(self.NotationValue)+','

        return line
