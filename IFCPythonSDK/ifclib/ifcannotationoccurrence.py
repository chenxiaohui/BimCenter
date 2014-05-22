#!/usr/bin/python
#coding=utf-8
#Filename:IfcAnnotationOccurrence.py
import log
import common
from ifcstyleditem import IFCSTYLEDITEM

from utils import *

class IFCANNOTATIONOCCURRENCE(IFCSTYLEDITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCANNOTATIONOCCURRENCE,self).__init__(id,arg)
        self.type='IFCANNOTATIONOCCURRENCE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCANNOTATIONOCCURRENCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCANNOTATIONOCCURRENCE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCANNOTATIONOCCURRENCE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCANNOTATIONOCCURRENCE,self).toString()       

        return line
