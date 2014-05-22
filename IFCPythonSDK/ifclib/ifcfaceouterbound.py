#!/usr/bin/python
#coding=utf-8
#Filename:IfcFaceOuterBound.py
import log
import common
from ifcfacebound import IFCFACEBOUND

from utils import *

class IFCFACEOUTERBOUND(IFCFACEBOUND):
    """"""
    def __init__(self,id,arg):
        super(IFCFACEOUTERBOUND,self).__init__(id,arg)
        self.type='IFCFACEOUTERBOUND'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFACEOUTERBOUND,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFACEOUTERBOUND,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFACEOUTERBOUND,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFACEOUTERBOUND,self).toString()       

        return line
