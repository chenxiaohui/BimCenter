#!/usr/bin/python
#coding=utf-8
#Filename:IfcTwoDirectionRepeatFactor.py
import log
import common
from ifconedirectionrepeatfactor import IFCONEDIRECTIONREPEATFACTOR

from utils import *

class IFCTWODIRECTIONREPEATFACTOR(IFCONEDIRECTIONREPEATFACTOR):
    """"""
    def __init__(self,id,arg):
        super(IFCTWODIRECTIONREPEATFACTOR,self).__init__(id,arg)
        self.type='IFCTWODIRECTIONREPEATFACTOR'
        self.inverse={}
        self.SecondRepeatFactor=None #IfcVector


    def load(self):
        """register inverses"""
        if not super(IFCTWODIRECTIONREPEATFACTOR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTWODIRECTIONREPEATFACTOR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SecondRepeatFactor= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTWODIRECTIONREPEATFACTOR,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCTWODIRECTIONREPEATFACTOR,self).toString()       
        line += idToSPF(self.SecondRepeatFactor)+','

        return line
