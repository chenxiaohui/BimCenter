#!/usr/bin/python
#coding=utf-8
#Filename:IfcCartesianTransformationOperator2DnonUniform.py
import log
import common
from ifccartesiantransformationoperator2d import IFCCARTESIANTRANSFORMATIONOPERATOR2D

from utils import *

class IFCCARTESIANTRANSFORMATIONOPERATOR2DNONUNIFORM(IFCCARTESIANTRANSFORMATIONOPERATOR2D):
    """"""
    def __init__(self,id,arg):
        super(IFCCARTESIANTRANSFORMATIONOPERATOR2DNONUNIFORM,self).__init__(id,arg)
        self.type='IFCCARTESIANTRANSFORMATIONOPERATOR2DNONUNIFORM'
        self.inverse={}
        self.Scale2=None #REAL


    def load(self):
        """register inverses"""
        if not super(IFCCARTESIANTRANSFORMATIONOPERATOR2DNONUNIFORM,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCARTESIANTRANSFORMATIONOPERATOR2DNONUNIFORM,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Scale2= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCARTESIANTRANSFORMATIONOPERATOR2DNONUNIFORM,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCARTESIANTRANSFORMATIONOPERATOR2DNONUNIFORM,self).toString()       
        line += integerToSPF(self.Scale2)+','

        return line
