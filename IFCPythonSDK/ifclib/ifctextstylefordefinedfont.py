#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextStyleForDefinedFont.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCTEXTSTYLEFORDEFINEDFONT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCTEXTSTYLEFORDEFINEDFONT,self).__init__(id,arg)
        self.type='IFCTEXTSTYLEFORDEFINEDFONT'
        self.inverse={}
        self.Colour=None #IfcColour
        self.BackgroundColour=None #IfcColour


    def load(self):
        """register inverses"""
        if not super(IFCTEXTSTYLEFORDEFINEDFONT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTEXTSTYLEFORDEFINEDFONT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Colour= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BackgroundColour= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTEXTSTYLEFORDEFINEDFONT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCTEXTSTYLEFORDEFINEDFONT,self).toString()       
        line += typerefToSPF(self.Colour)+','
        line += typerefToSPF(self.BackgroundColour)+','

        return line
