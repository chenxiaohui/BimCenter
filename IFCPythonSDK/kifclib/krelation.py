#!/usr/bin/python
#coding=utf-8
#Filename:KRelation.py
import log
import common
from kroot import KROOT

from utils import *

class KRELATION(KROOT):
    """"""
    def __init__(self,id,arg):
        super(KRELATION,self).__init__(id,arg)
        self.type='KRELATION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(KRELATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(KRELATION,self).init():
            return False

        return True

    def getAttrCount(self):
        """"""
        return super(KRELATION,self).getAttrCount()+0
