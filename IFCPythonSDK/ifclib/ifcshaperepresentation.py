#!/usr/bin/python
#coding=utf-8
#Filename:IfcShapeRepresentation.py
import log
import common
from ifcshapemodel import IFCSHAPEMODEL

from utils import *

class IFCSHAPEREPRESENTATION(IFCSHAPEMODEL):
    """"""
    def __init__(self,id,arg):
        super(IFCSHAPEREPRESENTATION,self).__init__(id,arg)
        self.type='IFCSHAPEREPRESENTATION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSHAPEREPRESENTATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSHAPEREPRESENTATION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSHAPEREPRESENTATION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSHAPEREPRESENTATION,self).toString()       

        return line
