#!/usr/bin/python
#coding=utf-8
#Filename:KDimension.py
import log
import common
from kroot import KROOT

from utils import *

class KDIMENSION(KROOT):
    """"""
    def __init__(self,id,arg):
        super(KDIMENSION,self).__init__(id,arg)
        self.type='KDIMENSION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(KDIMENSION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(KDIMENSION,self).init():
            return False

        return True

    def getAttrCount(self):
        """"""
        return super(KDIMENSION,self).getAttrCount()+0
