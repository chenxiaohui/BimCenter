#!/usr/bin/python
#coding=utf-8
#Filename:IfcElementAssembly.py
import log
import common
from ifcelement import IFCELEMENT

from utils import *

class IFCELEMENTASSEMBLY(IFCELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCELEMENTASSEMBLY,self).__init__(id,arg)
        self.type='IFCELEMENTASSEMBLY'
        self.inverse={}
        self.AssemblyPlace=None #IfcAssemblyPlaceEnum
        self.PredefinedType=None #IfcElementAssemblyTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCELEMENTASSEMBLY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELEMENTASSEMBLY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AssemblyPlace= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELEMENTASSEMBLY,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCELEMENTASSEMBLY,self).toString()       
        line += typerefToSPF(self.AssemblyPlace)+','
        line += typerefToSPF(self.PredefinedType)+','

        return line
