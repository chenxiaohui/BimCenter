#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelOccupiesSpaces.py
import log
import common
from ifcrelassignstoactor import IFCRELASSIGNSTOACTOR

from utils import *

class IFCRELOCCUPIESSPACES(IFCRELASSIGNSTOACTOR):
    """"""
    def __init__(self,id,arg):
        super(IFCRELOCCUPIESSPACES,self).__init__(id,arg)
        self.type='IFCRELOCCUPIESSPACES'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCRELOCCUPIESSPACES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELOCCUPIESSPACES,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELOCCUPIESSPACES,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCRELOCCUPIESSPACES,self).toString()       

        return line
