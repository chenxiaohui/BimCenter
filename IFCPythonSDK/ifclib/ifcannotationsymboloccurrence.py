#!/usr/bin/python
#coding=utf-8
#Filename:IfcAnnotationSymbolOccurrence.py
import log
import common
from ifcannotationoccurrence import IFCANNOTATIONOCCURRENCE

from utils import *

class IFCANNOTATIONSYMBOLOCCURRENCE(IFCANNOTATIONOCCURRENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCANNOTATIONSYMBOLOCCURRENCE,self).__init__(id,arg)
        self.type='IFCANNOTATIONSYMBOLOCCURRENCE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCANNOTATIONSYMBOLOCCURRENCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCANNOTATIONSYMBOLOCCURRENCE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCANNOTATIONSYMBOLOCCURRENCE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCANNOTATIONSYMBOLOCCURRENCE,self).toString()       

        return line
