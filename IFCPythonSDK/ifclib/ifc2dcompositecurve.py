#!/usr/bin/python
#coding=utf-8
#Filename:Ifc2DCompositeCurve.py
import log
import common
from ifccompositecurve import IFCCOMPOSITECURVE

from utils import *

class IFC2DCOMPOSITECURVE(IFCCOMPOSITECURVE):
    """"""
    def __init__(self,id,arg):
        super(IFC2DCOMPOSITECURVE,self).__init__(id,arg)
        self.type='IFC2DCOMPOSITECURVE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFC2DCOMPOSITECURVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFC2DCOMPOSITECURVE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFC2DCOMPOSITECURVE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFC2DCOMPOSITECURVE,self).toString()       

        return line
