#!/usr/bin/python
#coding=utf-8
#Filename:IfcBooleanClippingResult.py
import log
import common
from ifcbooleanresult import IFCBOOLEANRESULT

from utils import *

class IFCBOOLEANCLIPPINGRESULT(IFCBOOLEANRESULT):
    """"""
    def __init__(self,id,arg):
        super(IFCBOOLEANCLIPPINGRESULT,self).__init__(id,arg)
        self.type='IFCBOOLEANCLIPPINGRESULT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCBOOLEANCLIPPINGRESULT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBOOLEANCLIPPINGRESULT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBOOLEANCLIPPINGRESULT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCBOOLEANCLIPPINGRESULT,self).toString()       

        return line
