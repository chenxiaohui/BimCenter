#!/usr/bin/python
#coding=utf-8
#Filename:IfcArbitraryOpenProfileDef.py
import log
import common
from ifcprofiledef import IFCPROFILEDEF

from utils import *

class IFCARBITRARYOPENPROFILEDEF(IFCPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCARBITRARYOPENPROFILEDEF,self).__init__(id,arg)
        self.type='IFCARBITRARYOPENPROFILEDEF'
        self.inverse={}
        self.Curve=None #IfcBoundedCurve


    def load(self):
        """register inverses"""
        if not super(IFCARBITRARYOPENPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCARBITRARYOPENPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Curve= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCARBITRARYOPENPROFILEDEF,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCARBITRARYOPENPROFILEDEF,self).toString()       
        line += idToSPF(self.Curve)+','

        return line
