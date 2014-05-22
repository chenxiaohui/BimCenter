#!/usr/bin/python
#coding=utf-8
#Filename:IfcMaterialList.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCMATERIALLIST(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCMATERIALLIST,self).__init__(id,arg)
        self.type='IFCMATERIALLIST'
        self.inverse={}
        self.Materials=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCMATERIALLIST,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMATERIALLIST,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Materials= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMATERIALLIST,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCMATERIALLIST,self).toString()       
        line += listParamToSPF(self.Materials,idToSPF)+','

        return line
