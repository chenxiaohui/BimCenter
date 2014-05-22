#!/usr/bin/python
#coding=utf-8
#Filename:IfcGroup.py
import log
import common
from ifcobject import IFCOBJECT

from utils import *

class IFCGROUP(IFCOBJECT):
    """"""
    def __init__(self,id,arg):
        super(IFCGROUP,self).__init__(id,arg)
        self.type='IFCGROUP'
        self.inverse={}
        self.inverse['IsGroupedBy']=[] #inverse:IfcRelAssignsToGroup of Alone


    def load(self):
        """register inverses"""
        if not super(IFCGROUP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGROUP,self).init():
            return False

        inverses = self.args.getInverses('IFCRELASSIGNSTOGROUP', 'RelatingGroup');
        if inverses:
            self.inverse['IsGroupedBy']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGROUP,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCGROUP,self).toString()       

        return line
