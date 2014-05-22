#!/usr/bin/python
#coding=utf-8
#Filename:IfcVirtualElement.py
import log
import common
from ifcelement import IFCELEMENT

from utils import *

class IFCVIRTUALELEMENT(IFCELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCVIRTUALELEMENT,self).__init__(id,arg)
        self.type='IFCVIRTUALELEMENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCVIRTUALELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCVIRTUALELEMENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCVIRTUALELEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCVIRTUALELEMENT,self).toString()       

        return line
