#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralSurfaceConnection.py
import log
import common
from ifcstructuralconnection import IFCSTRUCTURALCONNECTION

from utils import *

class IFCSTRUCTURALSURFACECONNECTION(IFCSTRUCTURALCONNECTION):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALSURFACECONNECTION,self).__init__(id,arg)
        self.type='IFCSTRUCTURALSURFACECONNECTION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALSURFACECONNECTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALSURFACECONNECTION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALSURFACECONNECTION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALSURFACECONNECTION,self).toString()       

        return line
