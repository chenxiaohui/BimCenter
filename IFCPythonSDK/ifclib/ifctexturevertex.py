#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextureVertex.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCTEXTUREVERTEX(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCTEXTUREVERTEX,self).__init__(id,arg)
        self.type='IFCTEXTUREVERTEX'
        self.inverse={}
        self.Coordinates=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCTEXTUREVERTEX,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTEXTUREVERTEX,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Coordinates= getIdListParam(arg,spfToInteger)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTEXTUREVERTEX,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCTEXTUREVERTEX,self).toString()       
        line += listParamToSPF(self.Coordinates,integerToSPF)+','

        return line
