#!/usr/bin/python
#coding=utf-8
#Filename:IfcConstructionEquipmentResource.py
import log
import common
from ifcconstructionresource import IFCCONSTRUCTIONRESOURCE

from utils import *

class IFCCONSTRUCTIONEQUIPMENTRESOURCE(IFCCONSTRUCTIONRESOURCE):
    """"""
    def __init__(self,id,arg):
        super(IFCCONSTRUCTIONEQUIPMENTRESOURCE,self).__init__(id,arg)
        self.type='IFCCONSTRUCTIONEQUIPMENTRESOURCE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCCONSTRUCTIONEQUIPMENTRESOURCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONSTRUCTIONEQUIPMENTRESOURCE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONSTRUCTIONEQUIPMENTRESOURCE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCONSTRUCTIONEQUIPMENTRESOURCE,self).toString()       

        return line
