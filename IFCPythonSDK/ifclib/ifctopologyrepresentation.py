#!/usr/bin/python
#coding=utf-8
#Filename:IfcTopologyRepresentation.py
import log
import common
from ifcshapemodel import IFCSHAPEMODEL

from utils import *

class IFCTOPOLOGYREPRESENTATION(IFCSHAPEMODEL):
    """"""
    def __init__(self,id,arg):
        super(IFCTOPOLOGYREPRESENTATION,self).__init__(id,arg)
        self.type='IFCTOPOLOGYREPRESENTATION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCTOPOLOGYREPRESENTATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTOPOLOGYREPRESENTATION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTOPOLOGYREPRESENTATION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCTOPOLOGYREPRESENTATION,self).toString()       

        return line
