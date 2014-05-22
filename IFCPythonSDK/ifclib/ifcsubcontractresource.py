#!/usr/bin/python
#coding=utf-8
#Filename:IfcSubContractResource.py
import log
import common
from ifcconstructionresource import IFCCONSTRUCTIONRESOURCE

from utils import *

class IFCSUBCONTRACTRESOURCE(IFCCONSTRUCTIONRESOURCE):
    """"""
    def __init__(self,id,arg):
        super(IFCSUBCONTRACTRESOURCE,self).__init__(id,arg)
        self.type='IFCSUBCONTRACTRESOURCE'
        self.inverse={}
        self.SubContractor=None #IfcActorSelect
        self.JobDescription=None #IfcText


    def load(self):
        """register inverses"""
        if not super(IFCSUBCONTRACTRESOURCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSUBCONTRACTRESOURCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SubContractor= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.JobDescription= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSUBCONTRACTRESOURCE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSUBCONTRACTRESOURCE,self).toString()       
        line += typerefToSPF(self.SubContractor)+','
        line += strToSPF(self.JobDescription)+','

        return line
