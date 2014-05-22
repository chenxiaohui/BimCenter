#!/usr/bin/python
#coding=utf-8
#Filename:IfcParameterizedProfileDef.py
import log
import common
from ifcprofiledef import IFCPROFILEDEF

from utils import *

class IFCPARAMETERIZEDPROFILEDEF(IFCPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCPARAMETERIZEDPROFILEDEF,self).__init__(id,arg)
        self.type='IFCPARAMETERIZEDPROFILEDEF'
        self.inverse={}
        self.Position=None #IfcAxis2Placement2D


    def load(self):
        """register inverses"""
        if not super(IFCPARAMETERIZEDPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPARAMETERIZEDPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Position= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPARAMETERIZEDPROFILEDEF,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPARAMETERIZEDPROFILEDEF,self).toString()       
        line += idToSPF(self.Position)+','

        return line
