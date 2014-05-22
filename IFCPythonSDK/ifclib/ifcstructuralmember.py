#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralMember.py
import log
import common
from ifcstructuralitem import IFCSTRUCTURALITEM

from utils import *

class IFCSTRUCTURALMEMBER(IFCSTRUCTURALITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALMEMBER,self).__init__(id,arg)
        self.type='IFCSTRUCTURALMEMBER'
        self.inverse={}
        self.inverse['ConnectedBy']=[] #inverse:SET of IfcRelConnectsStructuralMember
        self.inverse['ReferencesElement']=[] #inverse:SET of IfcRelConnectsStructuralElement


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALMEMBER,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALMEMBER,self).init():
            return False

        inverses = self.args.getInverses('IFCRELCONNECTSSTRUCTURALMEMBER', 'RelatingStructuralMember');
        if inverses:
            self.inverse['ConnectedBy']=inverses

        inverses = self.args.getInverses('IFCRELCONNECTSSTRUCTURALELEMENT', 'RelatedStructuralMember');
        if inverses:
            self.inverse['ReferencesElement']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALMEMBER,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALMEMBER,self).toString()       

        return line
