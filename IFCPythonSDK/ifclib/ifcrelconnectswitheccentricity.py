#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelConnectsWithEccentricity.py
import log
import common
from ifcrelconnectsstructuralmember import IFCRELCONNECTSSTRUCTURALMEMBER

from utils import *

class IFCRELCONNECTSWITHECCENTRICITY(IFCRELCONNECTSSTRUCTURALMEMBER):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCONNECTSWITHECCENTRICITY,self).__init__(id,arg)
        self.type='IFCRELCONNECTSWITHECCENTRICITY'
        self.inverse={}
        self.ConnectionConstraint=None #IfcConnectionGeometry


    def load(self):
        """register inverses"""
        if not super(IFCRELCONNECTSWITHECCENTRICITY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCONNECTSWITHECCENTRICITY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConnectionConstraint= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCONNECTSWITHECCENTRICITY,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELCONNECTSWITHECCENTRICITY,self).toString()       
        line += idToSPF(self.ConnectionConstraint)+','

        return line
