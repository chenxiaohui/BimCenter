#!/usr/bin/python
#coding=utf-8
#Filename:IfcElectricalCircuit.py
import log
import common
from ifcsystem import IFCSYSTEM

from utils import *

class IFCELECTRICALCIRCUIT(IFCSYSTEM):
    """"""
    def __init__(self,id,arg):
        super(IFCELECTRICALCIRCUIT,self).__init__(id,arg)
        self.type='IFCELECTRICALCIRCUIT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCELECTRICALCIRCUIT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELECTRICALCIRCUIT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELECTRICALCIRCUIT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCELECTRICALCIRCUIT,self).toString()       

        return line
