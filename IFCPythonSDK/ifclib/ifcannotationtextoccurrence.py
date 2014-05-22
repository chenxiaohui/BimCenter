#!/usr/bin/python
#coding=utf-8
#Filename:IfcAnnotationTextOccurrence.py
import log
import common
from ifcannotationoccurrence import IFCANNOTATIONOCCURRENCE

from utils import *

class IFCANNOTATIONTEXTOCCURRENCE(IFCANNOTATIONOCCURRENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCANNOTATIONTEXTOCCURRENCE,self).__init__(id,arg)
        self.type='IFCANNOTATIONTEXTOCCURRENCE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCANNOTATIONTEXTOCCURRENCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCANNOTATIONTEXTOCCURRENCE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCANNOTATIONTEXTOCCURRENCE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCANNOTATIONTEXTOCCURRENCE,self).toString()       

        return line
