#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssociatesConstraint.py
import log
import common
from ifcrelassociates import IFCRELASSOCIATES

from utils import *

class IFCRELASSOCIATESCONSTRAINT(IFCRELASSOCIATES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSOCIATESCONSTRAINT,self).__init__(id,arg)
        self.type='IFCRELASSOCIATESCONSTRAINT'
        self.inverse={}
        self.Intent=None #IfcLabel
        self.RelatingConstraint=None #IfcConstraint


    def load(self):
        """register inverses"""
        if not super(IFCRELASSOCIATESCONSTRAINT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSOCIATESCONSTRAINT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Intent= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingConstraint= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSOCIATESCONSTRAINT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELASSOCIATESCONSTRAINT,self).toString()       
        line += strToSPF(self.Intent)+','
        line += idToSPF(self.RelatingConstraint)+','

        return line
