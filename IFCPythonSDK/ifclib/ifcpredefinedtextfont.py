#!/usr/bin/python
#coding=utf-8
#Filename:IfcPreDefinedTextFont.py
import log
import common
from ifcpredefineditem import IFCPREDEFINEDITEM

from utils import *

class IFCPREDEFINEDTEXTFONT(IFCPREDEFINEDITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCPREDEFINEDTEXTFONT,self).__init__(id,arg)
        self.type='IFCPREDEFINEDTEXTFONT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPREDEFINEDTEXTFONT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPREDEFINEDTEXTFONT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPREDEFINEDTEXTFONT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPREDEFINEDTEXTFONT,self).toString()       

        return line
