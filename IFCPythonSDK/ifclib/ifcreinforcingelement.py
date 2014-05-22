#!/usr/bin/python
#coding=utf-8
#Filename:IfcReinforcingElement.py
import log
import common
from ifcbuildingelementcomponent import IFCBUILDINGELEMENTCOMPONENT

from utils import *

class IFCREINFORCINGELEMENT(IFCBUILDINGELEMENTCOMPONENT):
    """"""
    def __init__(self,id,arg):
        super(IFCREINFORCINGELEMENT,self).__init__(id,arg)
        self.type='IFCREINFORCINGELEMENT'
        self.inverse={}
        self.SteelGrade=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCREINFORCINGELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREINFORCINGELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SteelGrade= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREINFORCINGELEMENT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCREINFORCINGELEMENT,self).toString()       
        line += strToSPF(self.SteelGrade)+','

        return line
