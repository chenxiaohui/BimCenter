#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralActivity.py
import log
import common
from ifcproduct import IFCPRODUCT

from utils import *

class IFCSTRUCTURALACTIVITY(IFCPRODUCT):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALACTIVITY,self).__init__(id,arg)
        self.type='IFCSTRUCTURALACTIVITY'
        self.inverse={}
        self.AppliedLoad=None #IfcStructuralLoad
        self.GlobalOrLocal=None #IfcGlobalOrLocalEnum
        self.inverse['AssignedToStructuralItem']=[] #inverse:IfcRelConnectsStructuralActivity of Alone


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALACTIVITY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALACTIVITY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AppliedLoad= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.GlobalOrLocal= spfToTypeRef(arg)

        inverses = self.args.getInverses('IFCRELCONNECTSSTRUCTURALACTIVITY', 'RelatedStructuralActivity');
        if inverses:
            self.inverse['AssignedToStructuralItem']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALACTIVITY,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALACTIVITY,self).toString()       
        line += idToSPF(self.AppliedLoad)+','
        line += typerefToSPF(self.GlobalOrLocal)+','

        return line
