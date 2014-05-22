#!/usr/bin/python
#coding=utf-8
#Filename:IfcBeam.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCBEAM(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCBEAM,self).__init__(id,arg)
        self.type='IFCBEAM'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCBEAM,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBEAM,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBEAM,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCBEAM,self).toString()       

        return line
