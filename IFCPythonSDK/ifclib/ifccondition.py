#!/usr/bin/python
#coding=utf-8
#Filename:IfcCondition.py
import log
import common
from ifcgroup import IFCGROUP

from utils import *

class IFCCONDITION(IFCGROUP):
    """"""
    def __init__(self,id,arg):
        super(IFCCONDITION,self).__init__(id,arg)
        self.type='IFCCONDITION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCCONDITION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONDITION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONDITION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCONDITION,self).toString()       

        return line
