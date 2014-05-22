#!/usr/bin/python
#coding=utf-8
#Filename:KDrawings.py
import log
import common
from kdocument import KDOCUMENT

from utils import *

class KDRAWINGS(KDOCUMENT):
    """"""
    def __init__(self,id,arg):
        super(KDRAWINGS,self).__init__(id,arg)
        self.type='KDRAWINGS'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(KDRAWINGS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(KDRAWINGS,self).init():
            return False

        return True

    def getAttrCount(self):
        """"""
        return super(KDRAWINGS,self).getAttrCount()+0
