#!/usr/bin/python
#coding=utf-8
#Filename:IfcDiameterDimension.py
import log
import common
from ifcdimensioncurvedirectedcallout import IFCDIMENSIONCURVEDIRECTEDCALLOUT

from utils import *

class IFCDIAMETERDIMENSION(IFCDIMENSIONCURVEDIRECTEDCALLOUT):
    """"""
    def __init__(self,id,arg):
        super(IFCDIAMETERDIMENSION,self).__init__(id,arg)
        self.type='IFCDIAMETERDIMENSION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDIAMETERDIMENSION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDIAMETERDIMENSION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDIAMETERDIMENSION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDIAMETERDIMENSION,self).toString()       

        return line
