#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextStyle.py
import log
import common
from ifcpresentationstyle import IFCPRESENTATIONSTYLE

from utils import *

class IFCTEXTSTYLE(IFCPRESENTATIONSTYLE):
    """"""
    def __init__(self,id,arg):
        super(IFCTEXTSTYLE,self).__init__(id,arg)
        self.type='IFCTEXTSTYLE'
        self.inverse={}
        self.TextCharacterAppearance=None #IfcCharacterStyleSelect
        self.TextStyle=None #IfcTextStyleSelect
        self.TextFontStyle=None #IfcTextFontSelect


    def load(self):
        """register inverses"""
        if not super(IFCTEXTSTYLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTEXTSTYLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextCharacterAppearance= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextStyle= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextFontStyle= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTEXTSTYLE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCTEXTSTYLE,self).toString()       
        line += typerefToSPF(self.TextCharacterAppearance)+','
        line += typerefToSPF(self.TextStyle)+','
        line += typerefToSPF(self.TextFontStyle)+','

        return line
