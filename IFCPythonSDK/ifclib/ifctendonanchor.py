#!/usr/bin/python
#coding=utf-8
#Filename:IfcTendonAnchor.py
import log
import common
from ifcreinforcingelement import IFCREINFORCINGELEMENT

from utils import *

class IFCTENDONANCHOR(IFCREINFORCINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCTENDONANCHOR,self).__init__(id,arg)
        self.type='IFCTENDONANCHOR'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCTENDONANCHOR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTENDONANCHOR,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTENDONANCHOR,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCTENDONANCHOR,self).toString()       

        return line
