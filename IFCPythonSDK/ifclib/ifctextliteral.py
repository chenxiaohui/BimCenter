#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextLiteral.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCTEXTLITERAL(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCTEXTLITERAL,self).__init__(id,arg)
        self.type='IFCTEXTLITERAL'
        self.inverse={}
        self.Literal=None #IfcPresentableText
        self.Placement=None #IfcAxis2Placement
        self.Path=None #IfcTextPath


    def load(self):
        """register inverses"""
        if not super(IFCTEXTLITERAL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTEXTLITERAL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Literal= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Placement= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Path= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTEXTLITERAL,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCTEXTLITERAL,self).toString()       
        line += strToSPF(self.Literal)+','
        line += typerefToSPF(self.Placement)+','
        line += typerefToSPF(self.Path)+','

        return line
