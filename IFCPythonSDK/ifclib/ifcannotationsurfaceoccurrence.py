#!/usr/bin/python
#coding=utf-8
#Filename:IfcAnnotationSurfaceOccurrence.py
import log
import common
from ifcannotationoccurrence import IFCANNOTATIONOCCURRENCE

from utils import *

class IFCANNOTATIONSURFACEOCCURRENCE(IFCANNOTATIONOCCURRENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCANNOTATIONSURFACEOCCURRENCE,self).__init__(id,arg)
        self.type='IFCANNOTATIONSURFACEOCCURRENCE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCANNOTATIONSURFACEOCCURRENCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCANNOTATIONSURFACEOCCURRENCE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCANNOTATIONSURFACEOCCURRENCE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCANNOTATIONSURFACEOCCURRENCE,self).toString()       

        return line
