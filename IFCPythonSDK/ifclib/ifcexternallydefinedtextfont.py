#!/usr/bin/python
#coding=utf-8
#Filename:IfcExternallyDefinedTextFont.py
import log
import common
from ifcexternalreference import IFCEXTERNALREFERENCE

from utils import *

class IFCEXTERNALLYDEFINEDTEXTFONT(IFCEXTERNALREFERENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCEXTERNALLYDEFINEDTEXTFONT,self).__init__(id,arg)
        self.type='IFCEXTERNALLYDEFINEDTEXTFONT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCEXTERNALLYDEFINEDTEXTFONT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEXTERNALLYDEFINEDTEXTFONT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEXTERNALLYDEFINEDTEXTFONT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCEXTERNALLYDEFINEDTEXTFONT,self).toString()       

        return line
