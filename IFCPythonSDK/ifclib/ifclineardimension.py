#!/usr/bin/python
#coding=utf-8
#Filename:IfcLinearDimension.py
import log
import common
from ifcdimensioncurvedirectedcallout import IFCDIMENSIONCURVEDIRECTEDCALLOUT

from utils import *

class IFCLINEARDIMENSION(IFCDIMENSIONCURVEDIRECTEDCALLOUT):
    """"""
    def __init__(self,id,arg):
        super(IFCLINEARDIMENSION,self).__init__(id,arg)
        self.type='IFCLINEARDIMENSION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCLINEARDIMENSION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLINEARDIMENSION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLINEARDIMENSION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCLINEARDIMENSION,self).toString()       

        return line
