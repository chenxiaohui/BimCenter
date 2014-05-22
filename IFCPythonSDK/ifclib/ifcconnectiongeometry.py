#!/usr/bin/python
#coding=utf-8
#Filename:IfcConnectionGeometry.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCONNECTIONGEOMETRY(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCONNECTIONGEOMETRY,self).__init__(id,arg)
        self.type='IFCCONNECTIONGEOMETRY'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCCONNECTIONGEOMETRY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONNECTIONGEOMETRY,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONNECTIONGEOMETRY,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCONNECTIONGEOMETRY,self).toString()       

        return line
