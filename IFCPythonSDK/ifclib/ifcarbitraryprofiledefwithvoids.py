#!/usr/bin/python
#coding=utf-8
#Filename:IfcArbitraryProfileDefWithVoids.py
import log
import common
from ifcarbitraryclosedprofiledef import IFCARBITRARYCLOSEDPROFILEDEF

from utils import *

class IFCARBITRARYPROFILEDEFWITHVOIDS(IFCARBITRARYCLOSEDPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCARBITRARYPROFILEDEFWITHVOIDS,self).__init__(id,arg)
        self.type='IFCARBITRARYPROFILEDEFWITHVOIDS'
        self.inverse={}
        self.InnerCurves=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCARBITRARYPROFILEDEFWITHVOIDS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCARBITRARYPROFILEDEFWITHVOIDS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InnerCurves= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCARBITRARYPROFILEDEFWITHVOIDS,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCARBITRARYPROFILEDEFWITHVOIDS,self).toString()       
        line += listParamToSPF(self.InnerCurves,idToSPF)+','

        return line
