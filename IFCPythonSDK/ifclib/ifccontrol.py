#!/usr/bin/python
#coding=utf-8
#Filename:IfcControl.py
import log
import common
from ifcobject import IFCOBJECT

from utils import *

class IFCCONTROL(IFCOBJECT):
    """"""
    def __init__(self,id,arg):
        super(IFCCONTROL,self).__init__(id,arg)
        self.type='IFCCONTROL'
        self.inverse={}
        self.inverse['Controls']=[] #inverse:SET of IfcRelAssignsToControl


    def load(self):
        """register inverses"""
        if not super(IFCCONTROL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONTROL,self).init():
            return False

        inverses = self.args.getInverses('IFCRELASSIGNSTOCONTROL', 'RelatingControl');
        if inverses:
            self.inverse['Controls']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONTROL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCONTROL,self).toString()       

        return line
