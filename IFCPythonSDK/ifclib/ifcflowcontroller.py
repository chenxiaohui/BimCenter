#!/usr/bin/python
#coding=utf-8
#Filename:IfcFlowController.py
import log
import common
from ifcdistributionflowelement import IFCDISTRIBUTIONFLOWELEMENT

from utils import *

class IFCFLOWCONTROLLER(IFCDISTRIBUTIONFLOWELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFLOWCONTROLLER,self).__init__(id,arg)
        self.type='IFCFLOWCONTROLLER'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCFLOWCONTROLLER,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFLOWCONTROLLER,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFLOWCONTROLLER,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFLOWCONTROLLER,self).toString()       

        return line
