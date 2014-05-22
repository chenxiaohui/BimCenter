#!/usr/bin/python
#coding=utf-8
#Filename:IfcDiscreteAccessoryType.py
import log
import common
from ifcelementcomponenttype import IFCELEMENTCOMPONENTTYPE

from utils import *

class IFCDISCRETEACCESSORYTYPE(IFCELEMENTCOMPONENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCDISCRETEACCESSORYTYPE,self).__init__(id,arg)
        self.type='IFCDISCRETEACCESSORYTYPE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDISCRETEACCESSORYTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDISCRETEACCESSORYTYPE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDISCRETEACCESSORYTYPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDISCRETEACCESSORYTYPE,self).toString()       

        return line
