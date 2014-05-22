#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLoad.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCSTRUCTURALLOAD(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLOAD,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLOAD'
        self.inverse={}
        self.Name=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLOAD,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLOAD,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALLOAD,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLOAD,self).toString()       
        line += strToSPF(self.Name)+','

        return line
