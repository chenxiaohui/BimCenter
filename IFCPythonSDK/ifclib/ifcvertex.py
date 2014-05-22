#!/usr/bin/python
#coding=utf-8
#Filename:IfcVertex.py
import log
import common
from ifctopologicalrepresentationitem import IFCTOPOLOGICALREPRESENTATIONITEM

from utils import *

class IFCVERTEX(IFCTOPOLOGICALREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCVERTEX,self).__init__(id,arg)
        self.type='IFCVERTEX'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCVERTEX,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCVERTEX,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCVERTEX,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCVERTEX,self).toString()       

        return line
