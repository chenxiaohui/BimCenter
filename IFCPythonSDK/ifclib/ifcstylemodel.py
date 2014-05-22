#!/usr/bin/python
#coding=utf-8
#Filename:IfcStyleModel.py
import log
import common
from ifcrepresentation import IFCREPRESENTATION

from utils import *

class IFCSTYLEMODEL(IFCREPRESENTATION):
    """"""
    def __init__(self,id,arg):
        super(IFCSTYLEMODEL,self).__init__(id,arg)
        self.type='IFCSTYLEMODEL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSTYLEMODEL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTYLEMODEL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTYLEMODEL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTYLEMODEL,self).toString()       

        return line
