#!/usr/bin/python
#coding=utf-8
#Filename:IfcOpeningElement.py
import log
import common
from ifcfeatureelementsubtraction import IFCFEATUREELEMENTSUBTRACTION

from utils import *

class IFCOPENINGELEMENT(IFCFEATUREELEMENTSUBTRACTION):
    """"""
    def __init__(self,id,arg):
        super(IFCOPENINGELEMENT,self).__init__(id,arg)
        self.type='IFCOPENINGELEMENT'
        self.inverse={}
        self.inverse['HasFillings']=[] #inverse:SET of IfcRelFillsElement


    def load(self):
        """register inverses"""
        if not super(IFCOPENINGELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCOPENINGELEMENT,self).init():
            return False

        inverses = self.args.getInverses('IFCRELFILLSELEMENT', 'RelatingOpeningElement');
        if inverses:
            self.inverse['HasFillings']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCOPENINGELEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCOPENINGELEMENT,self).toString()       

        return line
