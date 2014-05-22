#!/usr/bin/python
#coding=utf-8
#Filename:IfcFurnitureType.py
import log
import common
from ifcfurnishingelementtype import IFCFURNISHINGELEMENTTYPE

from utils import *

class IFCFURNITURETYPE(IFCFURNISHINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCFURNITURETYPE,self).__init__(id,arg)
        self.type='IFCFURNITURETYPE'
        self.inverse={}
        self.AssemblyPlace=None #IfcAssemblyPlaceEnum


    def load(self):
        """register inverses"""
        if not super(IFCFURNITURETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFURNITURETYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AssemblyPlace= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFURNITURETYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFURNITURETYPE,self).toString()       
        line += typerefToSPF(self.AssemblyPlace)+','

        return line
