#!/usr/bin/python
#coding=utf-8
#Filename:IfcZone.py
import log
import common
from ifcgroup import IFCGROUP

from utils import *

class IFCZONE(IFCGROUP):
    """"""
    def __init__(self,id,arg):
        super(IFCZONE,self).__init__(id,arg)
        self.type='IFCZONE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCZONE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCZONE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCZONE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCZONE,self).toString()       

        return line
