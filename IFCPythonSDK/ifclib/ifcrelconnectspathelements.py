#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelConnectsPathElements.py
import log
import common
from ifcrelconnectselements import IFCRELCONNECTSELEMENTS

from utils import *

class IFCRELCONNECTSPATHELEMENTS(IFCRELCONNECTSELEMENTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCONNECTSPATHELEMENTS,self).__init__(id,arg)
        self.type='IFCRELCONNECTSPATHELEMENTS'
        self.inverse={}
        self.RelatingPriorities=None #LIST
        self.RelatedPriorities=None #LIST
        self.RelatedConnectionType=None #IfcConnectionTypeEnum
        self.RelatingConnectionType=None #IfcConnectionTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCRELCONNECTSPATHELEMENTS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCONNECTSPATHELEMENTS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingPriorities= getIdListParam(arg,spfToInteger)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedPriorities= getIdListParam(arg,spfToInteger)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedConnectionType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingConnectionType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCONNECTSPATHELEMENTS,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCRELCONNECTSPATHELEMENTS,self).toString()       
        line += listParamToSPF(self.RelatingPriorities,integerToSPF)+','
        line += listParamToSPF(self.RelatedPriorities,integerToSPF)+','
        line += typerefToSPF(self.RelatedConnectionType)+','
        line += typerefToSPF(self.RelatingConnectionType)+','

        return line
