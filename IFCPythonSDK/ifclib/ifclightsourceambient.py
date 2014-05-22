#!/usr/bin/python
#coding=utf-8
#Filename:IfcLightSourceAmbient.py
import log
import common
from ifclightsource import IFCLIGHTSOURCE

from utils import *

class IFCLIGHTSOURCEAMBIENT(IFCLIGHTSOURCE):
    """"""
    def __init__(self,id,arg):
        super(IFCLIGHTSOURCEAMBIENT,self).__init__(id,arg)
        self.type='IFCLIGHTSOURCEAMBIENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCLIGHTSOURCEAMBIENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLIGHTSOURCEAMBIENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLIGHTSOURCEAMBIENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCLIGHTSOURCEAMBIENT,self).toString()       

        return line
