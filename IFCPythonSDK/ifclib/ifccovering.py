#!/usr/bin/python
#coding=utf-8
#Filename:IfcCovering.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCCOVERING(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCCOVERING,self).__init__(id,arg)
        self.type='IFCCOVERING'
        self.inverse={}
        self.PredefinedType=None #IfcCoveringTypeEnum
        self.inverse['CoversSpaces']=[] #inverse:SET of IfcRelCoversSpaces
        self.inverse['Covers']=[] #inverse:SET of IfcRelCoversBldgElements


    def load(self):
        """register inverses"""
        if not super(IFCCOVERING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOVERING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        inverses = self.args.getInverses('IFCRELCOVERSSPACES', 'RelatedCoverings');
        if inverses:
            self.inverse['CoversSpaces']=inverses

        inverses = self.args.getInverses('IFCRELCOVERSBLDGELEMENTS', 'RelatedCoverings');
        if inverses:
            self.inverse['Covers']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOVERING,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCOVERING,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line
