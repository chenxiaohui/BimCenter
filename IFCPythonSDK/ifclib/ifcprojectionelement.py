#!/usr/bin/python
#coding=utf-8
#Filename:IfcProjectionElement.py
import log
import common
from ifcfeatureelementaddition import IFCFEATUREELEMENTADDITION

from utils import *

class IFCPROJECTIONELEMENT(IFCFEATUREELEMENTADDITION):
    """"""
    def __init__(self,id,arg):
        super(IFCPROJECTIONELEMENT,self).__init__(id,arg)
        self.type='IFCPROJECTIONELEMENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPROJECTIONELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROJECTIONELEMENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROJECTIONELEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPROJECTIONELEMENT,self).toString()       

        return line
