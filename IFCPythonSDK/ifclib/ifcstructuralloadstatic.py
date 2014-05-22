#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLoadStatic.py
import log
import common
from ifcstructuralload import IFCSTRUCTURALLOAD

from utils import *

class IFCSTRUCTURALLOADSTATIC(IFCSTRUCTURALLOAD):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLOADSTATIC,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLOADSTATIC'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLOADSTATIC,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLOADSTATIC,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALLOADSTATIC,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLOADSTATIC,self).toString()       

        return line
