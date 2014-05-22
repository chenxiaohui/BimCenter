#!/usr/bin/python
#coding=utf-8
#Filename:IfcAngularDimension.py
import log
import common
from ifcdimensioncurvedirectedcallout import IFCDIMENSIONCURVEDIRECTEDCALLOUT

from utils import *

class IFCANGULARDIMENSION(IFCDIMENSIONCURVEDIRECTEDCALLOUT):
    """"""
    def __init__(self,id,arg):
        super(IFCANGULARDIMENSION,self).__init__(id,arg)
        self.type='IFCANGULARDIMENSION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCANGULARDIMENSION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCANGULARDIMENSION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCANGULARDIMENSION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCANGULARDIMENSION,self).toString()       

        return line
