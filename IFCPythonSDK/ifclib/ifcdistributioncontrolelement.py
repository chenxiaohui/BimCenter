#!/usr/bin/python
#coding=utf-8
#Filename:IfcDistributionControlElement.py
import log
import common
from ifcdistributionelement import IFCDISTRIBUTIONELEMENT

from utils import *

class IFCDISTRIBUTIONCONTROLELEMENT(IFCDISTRIBUTIONELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCDISTRIBUTIONCONTROLELEMENT,self).__init__(id,arg)
        self.type='IFCDISTRIBUTIONCONTROLELEMENT'
        self.inverse={}
        self.ControlElementId=None #IfcIdentifier
        self.inverse['AssignedToFlowElement']=[] #inverse:SET of IfcRelFlowControlElements


    def load(self):
        """register inverses"""
        if not super(IFCDISTRIBUTIONCONTROLELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDISTRIBUTIONCONTROLELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ControlElementId= fromSPF(arg)

        inverses = self.args.getInverses('IFCRELFLOWCONTROLELEMENTS', 'RelatedControlElements');
        if inverses:
            self.inverse['AssignedToFlowElement']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDISTRIBUTIONCONTROLELEMENT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCDISTRIBUTIONCONTROLELEMENT,self).toString()       
        line += strToSPF(self.ControlElementId)+','

        return line
