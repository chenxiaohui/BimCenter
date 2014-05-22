#!/usr/bin/python
#coding=utf-8
#Filename:IfcAnnotationCurveOccurrence.py
import log
import common
from ifcannotationoccurrence import IFCANNOTATIONOCCURRENCE

from utils import *

class IFCANNOTATIONCURVEOCCURRENCE(IFCANNOTATIONOCCURRENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCANNOTATIONCURVEOCCURRENCE,self).__init__(id,arg)
        self.type='IFCANNOTATIONCURVEOCCURRENCE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCANNOTATIONCURVEOCCURRENCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCANNOTATIONCURVEOCCURRENCE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCANNOTATIONCURVEOCCURRENCE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCANNOTATIONCURVEOCCURRENCE,self).toString()       

        return line
