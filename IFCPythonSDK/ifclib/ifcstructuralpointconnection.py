#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralPointConnection.py
import log
import common
from ifcstructuralconnection import IFCSTRUCTURALCONNECTION

from utils import *

class IFCSTRUCTURALPOINTCONNECTION(IFCSTRUCTURALCONNECTION):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALPOINTCONNECTION,self).__init__(id,arg)
        self.type='IFCSTRUCTURALPOINTCONNECTION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALPOINTCONNECTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALPOINTCONNECTION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALPOINTCONNECTION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALPOINTCONNECTION,self).toString()       

        return line
