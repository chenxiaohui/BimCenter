#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssociatesMaterial.py
import log
import common
from ifcrelassociates import IFCRELASSOCIATES

from utils import *

class IFCRELASSOCIATESMATERIAL(IFCRELASSOCIATES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSOCIATESMATERIAL,self).__init__(id,arg)
        self.type='IFCRELASSOCIATESMATERIAL'
        self.inverse={}
        self.RelatingMaterial=None #IfcMaterialSelect


    def load(self):
        """register inverses"""
        if not super(IFCRELASSOCIATESMATERIAL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSOCIATESMATERIAL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingMaterial= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSOCIATESMATERIAL,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSOCIATESMATERIAL,self).toString()       
        line += typerefToSPF(self.RelatingMaterial)+','

        return line
