#!/usr/bin/python
#coding=utf-8
#Filename:IfcDistributionFlowElement.py
import log
import common
from ifcdistributionelement import IFCDISTRIBUTIONELEMENT

from utils import *

class IFCDISTRIBUTIONFLOWELEMENT(IFCDISTRIBUTIONELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCDISTRIBUTIONFLOWELEMENT,self).__init__(id,arg)
        self.type='IFCDISTRIBUTIONFLOWELEMENT'
        self.inverse={}
        self.inverse['HasControlElements']=[] #inverse:SET of IfcRelFlowControlElements


    def load(self):
        """register inverses"""
        if not super(IFCDISTRIBUTIONFLOWELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDISTRIBUTIONFLOWELEMENT,self).init():
            return False

        inverses = self.args.getInverses('IFCRELFLOWCONTROLELEMENTS', 'RelatingFlowElement');
        if inverses:
            self.inverse['HasControlElements']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDISTRIBUTIONFLOWELEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDISTRIBUTIONFLOWELEMENT,self).toString()       

        return line
