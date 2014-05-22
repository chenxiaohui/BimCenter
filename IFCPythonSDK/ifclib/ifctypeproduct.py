#!/usr/bin/python
#coding=utf-8
#Filename:IfcTypeProduct.py
import log
import common
from ifctypeobject import IFCTYPEOBJECT

from utils import *

class IFCTYPEPRODUCT(IFCTYPEOBJECT):
    """"""
    def __init__(self,id,arg):
        super(IFCTYPEPRODUCT,self).__init__(id,arg)
        self.type='IFCTYPEPRODUCT'
        self.inverse={}
        self.RepresentationMaps=None #LIST
        self.Tag=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCTYPEPRODUCT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTYPEPRODUCT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RepresentationMaps= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Tag= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTYPEPRODUCT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCTYPEPRODUCT,self).toString()       
        line += listParamToSPF(self.RepresentationMaps,idToSPF)+','
        line += strToSPF(self.Tag)+','

        return line
