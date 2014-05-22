#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextStyleTextModel.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCTEXTSTYLETEXTMODEL(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCTEXTSTYLETEXTMODEL,self).__init__(id,arg)
        self.type='IFCTEXTSTYLETEXTMODEL'
        self.inverse={}
        self.TextIndent=None #IfcSizeSelect
        self.TextAlign=None #IfcTextAlignment
        self.TextDecoration=None #IfcTextDecoration
        self.LetterSpacing=None #IfcSizeSelect
        self.WordSpacing=None #IfcSizeSelect
        self.TextTransform=None #IfcTextTransformation
        self.LineHeight=None #IfcSizeSelect


    def load(self):
        """register inverses"""
        if not super(IFCTEXTSTYLETEXTMODEL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTEXTSTYLETEXTMODEL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextIndent= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextAlign= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextDecoration= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LetterSpacing= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WordSpacing= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextTransform= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LineHeight= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTEXTSTYLETEXTMODEL,self).getAttrCount()+7

    def toString(self):
        """"""
        line=super(IFCTEXTSTYLETEXTMODEL,self).toString()       
        line += typerefToSPF(self.TextIndent)+','
        line += strToSPF(self.TextAlign)+','
        line += strToSPF(self.TextDecoration)+','
        line += typerefToSPF(self.LetterSpacing)+','
        line += typerefToSPF(self.WordSpacing)+','
        line += strToSPF(self.TextTransform)+','
        line += typerefToSPF(self.LineHeight)+','

        return line
