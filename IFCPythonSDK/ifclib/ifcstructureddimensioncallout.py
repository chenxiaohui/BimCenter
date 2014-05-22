#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuredDimensionCallout.py
import log
import common
from ifcdraughtingcallout import IFCDRAUGHTINGCALLOUT

from utils import *

class IFCSTRUCTUREDDIMENSIONCALLOUT(IFCDRAUGHTINGCALLOUT):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTUREDDIMENSIONCALLOUT,self).__init__(id,arg)
        self.type='IFCSTRUCTUREDDIMENSIONCALLOUT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTUREDDIMENSIONCALLOUT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTUREDDIMENSIONCALLOUT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTUREDDIMENSIONCALLOUT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTRUCTUREDDIMENSIONCALLOUT,self).toString()       

        return line
