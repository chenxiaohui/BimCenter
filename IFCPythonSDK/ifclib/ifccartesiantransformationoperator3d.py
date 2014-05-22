#!/usr/bin/python
#coding=utf-8
#Filename:IfcCartesianTransformationOperator3D.py
import log
import common
from ifccartesiantransformationoperator import IFCCARTESIANTRANSFORMATIONOPERATOR

from utils import *

class IFCCARTESIANTRANSFORMATIONOPERATOR3D(IFCCARTESIANTRANSFORMATIONOPERATOR):
    """"""
    def __init__(self,id,arg):
        super(IFCCARTESIANTRANSFORMATIONOPERATOR3D,self).__init__(id,arg)
        self.type='IFCCARTESIANTRANSFORMATIONOPERATOR3D'
        self.inverse={}
        self.Axis3=None #IfcDirection


    def load(self):
        """register inverses"""
        if not super(IFCCARTESIANTRANSFORMATIONOPERATOR3D,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCARTESIANTRANSFORMATIONOPERATOR3D,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Axis3= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCARTESIANTRANSFORMATIONOPERATOR3D,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCARTESIANTRANSFORMATIONOPERATOR3D,self).toString()       
        line += idToSPF(self.Axis3)+','

        return line
