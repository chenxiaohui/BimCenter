#!/usr/bin/python
#coding=utf-8
#Filename:IfcPath.py
import log
import common
from ifctopologicalrepresentationitem import IFCTOPOLOGICALREPRESENTATIONITEM

from utils import *

class IFCPATH(IFCTOPOLOGICALREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCPATH,self).__init__(id,arg)
        self.type='IFCPATH'
        self.inverse={}
        self.EdgeList=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCPATH,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPATH,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EdgeList= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPATH,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPATH,self).toString()       
        line += listParamToSPF(self.EdgeList,idToSPF)+','

        return line
