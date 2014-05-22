#!/usr/bin/python
#coding=utf-8
#Filename:IfcDerivedProfileDef.py
import log
import common
from ifcprofiledef import IFCPROFILEDEF

from utils import *

class IFCDERIVEDPROFILEDEF(IFCPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCDERIVEDPROFILEDEF,self).__init__(id,arg)
        self.type='IFCDERIVEDPROFILEDEF'
        self.inverse={}
        self.ParentProfile=None #IfcProfileDef
        self.Operator=None #IfcCartesianTransformationOperator2D
        self.Label=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCDERIVEDPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDERIVEDPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ParentProfile= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Operator= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Label= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDERIVEDPROFILEDEF,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCDERIVEDPROFILEDEF,self).toString()       
        line += idToSPF(self.ParentProfile)+','
        line += idToSPF(self.Operator)+','
        line += strToSPF(self.Label)+','

        return line
