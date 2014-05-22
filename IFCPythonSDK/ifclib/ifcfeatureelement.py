#!/usr/bin/python
#coding=utf-8
#Filename:IfcFeatureElement.py
import log
import common
from ifcelement import IFCELEMENT

from utils import *

class IFCFEATUREELEMENT(IFCELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFEATUREELEMENT,self).__init__(id,arg)
        self.type='IFCFEATUREELEMENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFEATUREELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFEATUREELEMENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFEATUREELEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFEATUREELEMENT,self).toString()       

        return line
