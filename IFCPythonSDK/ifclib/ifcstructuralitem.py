#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralItem.py
import log
import common
from ifcproduct import IFCPRODUCT

from utils import *

class IFCSTRUCTURALITEM(IFCPRODUCT):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALITEM,self).__init__(id,arg)
        self.type='IFCSTRUCTURALITEM'
        self.inverse={}
        self.inverse['AssignedStructuralActivity']=[] #inverse:SET of IfcRelConnectsStructuralActivity


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALITEM,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALITEM,self).init():
            return False

        inverses = self.args.getInverses('IFCRELCONNECTSSTRUCTURALACTIVITY', 'RelatingElement');
        if inverses:
            self.inverse['AssignedStructuralActivity']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALITEM,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALITEM,self).toString()       

        return line
