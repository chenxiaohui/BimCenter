#!/usr/bin/python
#coding=utf-8
#Filename:IfcTableRow.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCTABLEROW(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCTABLEROW,self).__init__(id,arg)
        self.type='IFCTABLEROW'
        self.inverse={}
        self.RowCells=None #LIST
        self.IsHeading=None #BOOLEAN
        self.inverse['OfTable']=[] #inverse:IfcTable of Alone


    def load(self):
        """register inverses"""
        if not super(IFCTABLEROW,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTABLEROW,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RowCells= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.IsHeading= spfToLogical(arg)

        inverses = self.args.getInverses('IFCTABLE', 'Rows');
        if inverses:
            self.inverse['OfTable']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTABLEROW,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCTABLEROW,self).toString()       
        line += listParamToSPF(self.RowCells,typerefToSPF)+','
        line += logicalToSPF(self.IsHeading)+','

        return line
