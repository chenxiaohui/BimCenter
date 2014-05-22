#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextureCoordinateGenerator.py
import log
import common
from ifctexturecoordinate import IFCTEXTURECOORDINATE

from utils import *

class IFCTEXTURECOORDINATEGENERATOR(IFCTEXTURECOORDINATE):
    """"""
    def __init__(self,id,arg):
        super(IFCTEXTURECOORDINATEGENERATOR,self).__init__(id,arg)
        self.type='IFCTEXTURECOORDINATEGENERATOR'
        self.inverse={}
        self.Mode=None #IfcLabel
        self.Parameter=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCTEXTURECOORDINATEGENERATOR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTEXTURECOORDINATEGENERATOR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Mode= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Parameter= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTEXTURECOORDINATEGENERATOR,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCTEXTURECOORDINATEGENERATOR,self).toString()       
        line += strToSPF(self.Mode)+','
        line += listParamToSPF(self.Parameter,typerefToSPF)+','

        return line
