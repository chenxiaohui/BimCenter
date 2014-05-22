#!/usr/bin/python
#coding=utf-8
#Filename:IfcCompositeProfileDef.py
import log
import common
from ifcprofiledef import IFCPROFILEDEF

from utils import *

class IFCCOMPOSITEPROFILEDEF(IFCPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCCOMPOSITEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCCOMPOSITEPROFILEDEF'
        self.inverse={}
        self.Profiles=None #SET
        self.Label=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCCOMPOSITEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOMPOSITEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Profiles= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Label= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOMPOSITEPROFILEDEF,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCOMPOSITEPROFILEDEF,self).toString()       
        line += listParamToSPF(self.Profiles,idToSPF)+','
        line += strToSPF(self.Label)+','

        return line
