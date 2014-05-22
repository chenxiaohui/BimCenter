#!/usr/bin/python
#coding=utf-8
#Filename:IfcPort.py
import log
import common
from ifcproduct import IFCPRODUCT

from utils import *

class IFCPORT(IFCPRODUCT):
    """"""
    def __init__(self,id,arg):
        super(IFCPORT,self).__init__(id,arg)
        self.type='IFCPORT'
        self.inverse={}
        self.inverse['ConnectedFrom']=[] #inverse:SET of IfcRelConnectsPorts
        self.inverse['ContainedIn']=[] #inverse:IfcRelConnectsPortToElement of Alone
        self.inverse['ConnectedTo']=[] #inverse:SET of IfcRelConnectsPorts


    def load(self):
        """register inverses"""
        if not super(IFCPORT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPORT,self).init():
            return False

        inverses = self.args.getInverses('IFCRELCONNECTSPORTS', 'RelatedPort');
        if inverses:
            self.inverse['ConnectedFrom']=inverses

        inverses = self.args.getInverses('IFCRELCONNECTSPORTTOELEMENT', 'RelatingPort');
        if inverses:
            self.inverse['ContainedIn']=inverses

        inverses = self.args.getInverses('IFCRELCONNECTSPORTS', 'RelatingPort');
        if inverses:
            self.inverse['ConnectedTo']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPORT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPORT,self).toString()       

        return line
