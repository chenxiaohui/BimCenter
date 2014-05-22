#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralPointReaction.py
import log
import common
from ifcstructuralreaction import IFCSTRUCTURALREACTION

from utils import *

class IFCSTRUCTURALPOINTREACTION(IFCSTRUCTURALREACTION):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALPOINTREACTION,self).__init__(id,arg)
        self.type='IFCSTRUCTURALPOINTREACTION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALPOINTREACTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALPOINTREACTION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALPOINTREACTION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALPOINTREACTION,self).toString()       

        return line
