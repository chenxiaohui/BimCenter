#!/usr/bin/python
#coding=utf-8
#Filename:IfcCsgSolid.py
import log
import common
from ifcsolidmodel import IFCSOLIDMODEL

from utils import *

class IFCCSGSOLID(IFCSOLIDMODEL):
    """"""
    def __init__(self,id,arg):
        super(IFCCSGSOLID,self).__init__(id,arg)
        self.type='IFCCSGSOLID'
        self.inverse={}
        self.TreeRootExpression=None #IfcCsgSelect


    def load(self):
        """register inverses"""
        if not super(IFCCSGSOLID,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCSGSOLID,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TreeRootExpression= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCSGSOLID,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCSGSOLID,self).toString()       
        line += typerefToSPF(self.TreeRootExpression)+','

        return line
