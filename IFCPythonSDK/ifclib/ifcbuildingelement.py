#!/usr/bin/python
#coding=utf-8
#Filename:IfcBuildingElement.py
import log
import common
from ifcelement import IFCELEMENT

from utils import *

class IFCBUILDINGELEMENT(IFCELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCBUILDINGELEMENT,self).__init__(id,arg)
        self.type='IFCBUILDINGELEMENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCBUILDINGELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBUILDINGELEMENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBUILDINGELEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCBUILDINGELEMENT,self).toString()       

        return line
