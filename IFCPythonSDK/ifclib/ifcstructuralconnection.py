#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralConnection.py
import log
import common
from ifcstructuralitem import IFCSTRUCTURALITEM

from utils import *

class IFCSTRUCTURALCONNECTION(IFCSTRUCTURALITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALCONNECTION,self).__init__(id,arg)
        self.type='IFCSTRUCTURALCONNECTION'
        self.inverse={}
        self.AppliedCondition=None #IfcBoundaryCondition
        self.inverse['ConnectsStructuralMembers']=[] #inverse:SET of IfcRelConnectsStructuralMember


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALCONNECTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALCONNECTION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AppliedCondition= spfToId(arg)

        inverses = self.args.getInverses('IFCRELCONNECTSSTRUCTURALMEMBER', 'RelatedStructuralConnection');
        if inverses:
            self.inverse['ConnectsStructuralMembers']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALCONNECTION,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALCONNECTION,self).toString()       
        line += idToSPF(self.AppliedCondition)+','

        return line
