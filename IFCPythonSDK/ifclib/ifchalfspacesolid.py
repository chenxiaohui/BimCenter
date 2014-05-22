#!/usr/bin/python
#coding=utf-8
#Filename:IfcHalfSpaceSolid.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCHALFSPACESOLID(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCHALFSPACESOLID,self).__init__(id,arg)
        self.type='IFCHALFSPACESOLID'
        self.inverse={}
        self.BaseSurface=None #IfcSurface
        self.AgreementFlag=None #BOOLEAN


    def load(self):
        """register inverses"""
        if not super(IFCHALFSPACESOLID,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCHALFSPACESOLID,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BaseSurface= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AgreementFlag= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCHALFSPACESOLID,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCHALFSPACESOLID,self).toString()       
        line += idToSPF(self.BaseSurface)+','
        line += logicalToSPF(self.AgreementFlag)+','

        return line
