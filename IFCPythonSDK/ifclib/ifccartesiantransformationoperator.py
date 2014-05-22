#!/usr/bin/python
#coding=utf-8
#Filename:IfcCartesianTransformationOperator.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCCARTESIANTRANSFORMATIONOPERATOR(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCCARTESIANTRANSFORMATIONOPERATOR,self).__init__(id,arg)
        self.type='IFCCARTESIANTRANSFORMATIONOPERATOR'
        self.inverse={}
        self.Axis1=None #IfcDirection
        self.Axis2=None #IfcDirection
        self.LocalOrigin=None #IfcCartesianPoint
        self.Scale=None #REAL


    def load(self):
        """register inverses"""
        if not super(IFCCARTESIANTRANSFORMATIONOPERATOR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCARTESIANTRANSFORMATIONOPERATOR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Axis1= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Axis2= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LocalOrigin= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Scale= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCARTESIANTRANSFORMATIONOPERATOR,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCCARTESIANTRANSFORMATIONOPERATOR,self).toString()       
        line += idToSPF(self.Axis1)+','
        line += idToSPF(self.Axis2)+','
        line += idToSPF(self.LocalOrigin)+','
        line += integerToSPF(self.Scale)+','

        return line
