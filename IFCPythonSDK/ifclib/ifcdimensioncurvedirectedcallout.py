#!/usr/bin/python
#coding=utf-8
#Filename:IfcDimensionCurveDirectedCallout.py
import log
import common
from ifcdraughtingcallout import IFCDRAUGHTINGCALLOUT

from utils import *

class IFCDIMENSIONCURVEDIRECTEDCALLOUT(IFCDRAUGHTINGCALLOUT):
    """"""
    def __init__(self,id,arg):
        super(IFCDIMENSIONCURVEDIRECTEDCALLOUT,self).__init__(id,arg)
        self.type='IFCDIMENSIONCURVEDIRECTEDCALLOUT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDIMENSIONCURVEDIRECTEDCALLOUT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDIMENSIONCURVEDIRECTEDCALLOUT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDIMENSIONCURVEDIRECTEDCALLOUT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDIMENSIONCURVEDIRECTEDCALLOUT,self).toString()       

        return line
