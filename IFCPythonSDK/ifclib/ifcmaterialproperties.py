#!/usr/bin/python
#coding=utf-8
#Filename:IfcMaterialProperties.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCMATERIALPROPERTIES(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCMATERIALPROPERTIES,self).__init__(id,arg)
        self.type='IFCMATERIALPROPERTIES'
        self.inverse={}
        self.Material=None #IfcMaterial


    def load(self):
        """register inverses"""
        if not super(IFCMATERIALPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMATERIALPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Material= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMATERIALPROPERTIES,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCMATERIALPROPERTIES,self).toString()       
        line += idToSPF(self.Material)+','

        return line
