#!/usr/bin/python
#coding=utf-8
#Filename:IfcDraughtingPreDefinedTextFont.py
import log
import common
from ifcpredefinedtextfont import IFCPREDEFINEDTEXTFONT

from utils import *

class IFCDRAUGHTINGPREDEFINEDTEXTFONT(IFCPREDEFINEDTEXTFONT):
    """"""
    def __init__(self,id,arg):
        super(IFCDRAUGHTINGPREDEFINEDTEXTFONT,self).__init__(id,arg)
        self.type='IFCDRAUGHTINGPREDEFINEDTEXTFONT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCDRAUGHTINGPREDEFINEDTEXTFONT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDRAUGHTINGPREDEFINEDTEXTFONT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDRAUGHTINGPREDEFINEDTEXTFONT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDRAUGHTINGPREDEFINEDTEXTFONT,self).toString()       

        return line
