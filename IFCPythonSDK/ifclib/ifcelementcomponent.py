#!/usr/bin/python
#coding=utf-8
#Filename:IfcElementComponent.py
import log
import common
from ifcelement import IFCELEMENT

from utils import *

class IFCELEMENTCOMPONENT(IFCELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCELEMENTCOMPONENT,self).__init__(id,arg)
        self.type='IFCELEMENTCOMPONENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCELEMENTCOMPONENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELEMENTCOMPONENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELEMENTCOMPONENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCELEMENTCOMPONENT,self).toString()       

        return line
