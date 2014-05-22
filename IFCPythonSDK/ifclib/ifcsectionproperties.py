#!/usr/bin/python
#coding=utf-8
#Filename:IfcSectionProperties.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCSECTIONPROPERTIES(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCSECTIONPROPERTIES,self).__init__(id,arg)
        self.type='IFCSECTIONPROPERTIES'
        self.inverse={}
        self.SectionType=None #IfcSectionTypeEnum
        self.StartProfile=None #IfcProfileDef
        self.EndProfile=None #IfcProfileDef


    def load(self):
        """register inverses"""
        if not super(IFCSECTIONPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSECTIONPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SectionType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.StartProfile= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EndProfile= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSECTIONPROPERTIES,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCSECTIONPROPERTIES,self).toString()       
        line += typerefToSPF(self.SectionType)+','
        line += idToSPF(self.StartProfile)+','
        line += idToSPF(self.EndProfile)+','

        return line
