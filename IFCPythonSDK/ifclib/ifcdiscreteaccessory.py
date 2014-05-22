#!/usr/bin/python
#coding=utf-8
#Filename:IfcDiscreteAccessory.py
import log
import common
from ifcelementcomponent import IFCELEMENTCOMPONENT

from utils import *

class IFCDISCRETEACCESSORY(IFCELEMENTCOMPONENT):
    """"""
    def __init__(self,id,arg):
        super(IFCDISCRETEACCESSORY,self).__init__(id,arg)
        self.type='IFCDISCRETEACCESSORY'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDISCRETEACCESSORY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDISCRETEACCESSORY,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDISCRETEACCESSORY,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDISCRETEACCESSORY,self).toString()       

        return line
