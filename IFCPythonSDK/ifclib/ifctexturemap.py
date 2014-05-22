#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextureMap.py
import log
import common
from ifctexturecoordinate import IFCTEXTURECOORDINATE

from utils import *

class IFCTEXTUREMAP(IFCTEXTURECOORDINATE):
    """"""
    def __init__(self,id,arg):
        super(IFCTEXTUREMAP,self).__init__(id,arg)
        self.type='IFCTEXTUREMAP'
        self.inverse={}
        self.TextureMaps=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCTEXTUREMAP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTEXTUREMAP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextureMaps= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTEXTUREMAP,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCTEXTUREMAP,self).toString()       
        line += listParamToSPF(self.TextureMaps,idToSPF)+','

        return line
