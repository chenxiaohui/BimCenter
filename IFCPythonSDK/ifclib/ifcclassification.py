#!/usr/bin/python
#coding=utf-8
#Filename:IfcClassification.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCLASSIFICATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCLASSIFICATION,self).__init__(id,arg)
        self.type='IFCCLASSIFICATION'
        self.inverse={}
        self.Source=None #IfcLabel
        self.Edition=None #IfcLabel
        self.EditionDate=None #IfcCalendarDate
        self.Name=None #IfcLabel
        self.inverse['Contains']=[] #inverse:SET of IfcClassificationItem


    def load(self):
        """register inverses"""
        if not super(IFCCLASSIFICATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCLASSIFICATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Source= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Edition= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.EditionDate= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        inverses = self.args.getInverses('IFCCLASSIFICATIONITEM', 'ItemOf');
        if inverses:
            self.inverse['Contains']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCLASSIFICATION,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCCLASSIFICATION,self).toString()       
        line += strToSPF(self.Source)+','
        line += strToSPF(self.Edition)+','
        line += idToSPF(self.EditionDate)+','
        line += strToSPF(self.Name)+','

        return line
