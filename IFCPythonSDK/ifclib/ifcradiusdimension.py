#!/usr/bin/python
#coding=utf-8
#Filename:IfcRadiusDimension.py
import log
import common
from ifcdimensioncurvedirectedcallout import IFCDIMENSIONCURVEDIRECTEDCALLOUT

from utils import *

class IFCRADIUSDIMENSION(IFCDIMENSIONCURVEDIRECTEDCALLOUT):
    """"""
    def __init__(self,id,arg):
        super(IFCRADIUSDIMENSION,self).__init__(id,arg)
        self.type='IFCRADIUSDIMENSION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCRADIUSDIMENSION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRADIUSDIMENSION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRADIUSDIMENSION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCRADIUSDIMENSION,self).toString()       

        return line
