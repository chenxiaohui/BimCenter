#!/usr/bin/python
#coding=utf-8
#Filename:IfcActor.py
import log
import common
from ifcobject import IFCOBJECT

from utils import *

class IFCACTOR(IFCOBJECT):
    """"""
    def __init__(self,id,arg):
        super(IFCACTOR,self).__init__(id,arg)
        self.type='IFCACTOR'
        self.inverse={}
        self.TheActor=None #IfcActorSelect
        self.inverse['IsActingUpon']=[] #inverse:SET of IfcRelAssignsToActor


    def load(self):
        """register inverses"""
        if not super(IFCACTOR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCACTOR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TheActor= spfToTypeRef(arg)

        inverses = self.args.getInverses('IFCRELASSIGNSTOACTOR', 'RelatingActor');
        if inverses:
            self.inverse['IsActingUpon']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCACTOR,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCACTOR,self).toString()       
        line += typerefToSPF(self.TheActor)+','

        return line
