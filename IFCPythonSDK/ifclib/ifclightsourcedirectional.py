#!/usr/bin/python
#coding=utf-8
#Filename:IfcLightSourceDirectional.py
import log
import common
from ifclightsource import IFCLIGHTSOURCE

from utils import *

class IFCLIGHTSOURCEDIRECTIONAL(IFCLIGHTSOURCE):
    """"""
    def __init__(self,id,arg):
        super(IFCLIGHTSOURCEDIRECTIONAL,self).__init__(id,arg)
        self.type='IFCLIGHTSOURCEDIRECTIONAL'
        self.inverse={}
        self.Orientation=None #IfcDirection


    def load(self):
        """register inverses"""
        if not super(IFCLIGHTSOURCEDIRECTIONAL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLIGHTSOURCEDIRECTIONAL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Orientation= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLIGHTSOURCEDIRECTIONAL,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCLIGHTSOURCEDIRECTIONAL,self).toString()       
        line += idToSPF(self.Orientation)+','

        return line
