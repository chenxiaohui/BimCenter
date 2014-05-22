#!/usr/bin/python
#coding=utf-8
#Filename:IfcAnnotationFillAreaOccurrence.py
import log
import common
from ifcannotationoccurrence import IFCANNOTATIONOCCURRENCE

from utils import *

class IFCANNOTATIONFILLAREAOCCURRENCE(IFCANNOTATIONOCCURRENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCANNOTATIONFILLAREAOCCURRENCE,self).__init__(id,arg)
        self.type='IFCANNOTATIONFILLAREAOCCURRENCE'
        self.inverse={}
        self.FillStyleTarget=None #IfcPoint
        self.GlobalOrLocal=None #IfcGlobalOrLocalEnum


    def load(self):
        """register inverses"""
        if not super(IFCANNOTATIONFILLAREAOCCURRENCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCANNOTATIONFILLAREAOCCURRENCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FillStyleTarget= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.GlobalOrLocal= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCANNOTATIONFILLAREAOCCURRENCE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCANNOTATIONFILLAREAOCCURRENCE,self).toString()       
        line += idToSPF(self.FillStyleTarget)+','
        line += typerefToSPF(self.GlobalOrLocal)+','

        return line
