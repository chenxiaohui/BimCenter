#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralReaction.py
import log
import common
from ifcstructuralactivity import IFCSTRUCTURALACTIVITY

from utils import *

class IFCSTRUCTURALREACTION(IFCSTRUCTURALACTIVITY):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALREACTION,self).__init__(id,arg)
        self.type='IFCSTRUCTURALREACTION'
        self.inverse={}
        self.inverse['Causes']=[] #inverse:SET of IfcStructuralAction


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALREACTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALREACTION,self).init():
            return False

        inverses = self.args.getInverses('IFCSTRUCTURALACTION', 'CausedBy');
        if inverses:
            self.inverse['Causes']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALREACTION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALREACTION,self).toString()       

        return line
