#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextStyleFontModel.py
import log
import common
from ifcpredefinedtextfont import IFCPREDEFINEDTEXTFONT

from utils import *

class IFCTEXTSTYLEFONTMODEL(IFCPREDEFINEDTEXTFONT):
    """"""
    def __init__(self,id,arg):
        super(IFCTEXTSTYLEFONTMODEL,self).__init__(id,arg)
        self.type='IFCTEXTSTYLEFONTMODEL'
        self.inverse={}
        self.FontFamily=None #LIST
        self.FontStyle=None #IfcFontStyle
        self.FontVariant=None #IfcFontVariant
        self.FontWeight=None #IfcFontWeight
        self.FontSize=None #IfcSizeSelect


    def load(self):
        """register inverses"""
        if not super(IFCTEXTSTYLEFONTMODEL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTEXTSTYLEFONTMODEL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FontFamily= getIdListParam(arg,fromSPF)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FontStyle= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FontVariant= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FontWeight= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FontSize= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTEXTSTYLEFONTMODEL,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCTEXTSTYLEFONTMODEL,self).toString()       
        line += listParamToSPF(self.FontFamily,strToSPF)+','
        line += strToSPF(self.FontStyle)+','
        line += strToSPF(self.FontVariant)+','
        line += strToSPF(self.FontWeight)+','
        line += typerefToSPF(self.FontSize)+','

        return line
