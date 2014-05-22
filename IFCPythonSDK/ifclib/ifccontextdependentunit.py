#!/usr/bin/python
#coding=utf-8
#Filename:IfcContextDependentUnit.py
import log
import common
from ifcnamedunit import IFCNAMEDUNIT

from utils import *

class IFCCONTEXTDEPENDENTUNIT(IFCNAMEDUNIT):
    """"""
    def __init__(self,id,arg):
        super(IFCCONTEXTDEPENDENTUNIT,self).__init__(id,arg)
        self.type='IFCCONTEXTDEPENDENTUNIT'
        self.inverse={}
        self.Name=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCCONTEXTDEPENDENTUNIT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONTEXTDEPENDENTUNIT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONTEXTDEPENDENTUNIT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCONTEXTDEPENDENTUNIT,self).toString()       
        line += strToSPF(self.Name)+','

        return line
