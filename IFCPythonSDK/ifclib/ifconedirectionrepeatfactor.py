#!/usr/bin/python
#coding=utf-8
#Filename:IfcOneDirectionRepeatFactor.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCONEDIRECTIONREPEATFACTOR(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCONEDIRECTIONREPEATFACTOR,self).__init__(id,arg)
        self.type='IFCONEDIRECTIONREPEATFACTOR'
        self.inverse={}
        self.RepeatFactor=None #IfcVector


    def load(self):
        """register inverses"""
        if not super(IFCONEDIRECTIONREPEATFACTOR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCONEDIRECTIONREPEATFACTOR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RepeatFactor= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCONEDIRECTIONREPEATFACTOR,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCONEDIRECTIONREPEATFACTOR,self).toString()       
        line += idToSPF(self.RepeatFactor)+','

        return line
