#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssignsToProjectOrder.py
import log
import common
from ifcrelassignstocontrol import IFCRELASSIGNSTOCONTROL

from utils import *

class IFCRELASSIGNSTOPROJECTORDER(IFCRELASSIGNSTOCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSIGNSTOPROJECTORDER,self).__init__(id,arg)
        self.type='IFCRELASSIGNSTOPROJECTORDER'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCRELASSIGNSTOPROJECTORDER,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSIGNSTOPROJECTORDER,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSIGNSTOPROJECTORDER,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCRELASSIGNSTOPROJECTORDER,self).toString()       

        return line
