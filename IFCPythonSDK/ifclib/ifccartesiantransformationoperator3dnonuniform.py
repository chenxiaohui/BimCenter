#!/usr/bin/python
#coding=utf-8
#Filename:IfcCartesianTransformationOperator3DnonUniform.py
import log
import common
from ifccartesiantransformationoperator3d import IFCCARTESIANTRANSFORMATIONOPERATOR3D

from utils import *

class IFCCARTESIANTRANSFORMATIONOPERATOR3DNONUNIFORM(IFCCARTESIANTRANSFORMATIONOPERATOR3D):
    """"""
    def __init__(self,id,arg):
        super(IFCCARTESIANTRANSFORMATIONOPERATOR3DNONUNIFORM,self).__init__(id,arg)
        self.type='IFCCARTESIANTRANSFORMATIONOPERATOR3DNONUNIFORM'
        self.inverse={}
        self.Scale2=None #REAL
        self.Scale3=None #REAL


    def load(self):
        """register inverses"""
        if not super(IFCCARTESIANTRANSFORMATIONOPERATOR3DNONUNIFORM,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCARTESIANTRANSFORMATIONOPERATOR3DNONUNIFORM,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Scale2= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Scale3= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCARTESIANTRANSFORMATIONOPERATOR3DNONUNIFORM,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCARTESIANTRANSFORMATIONOPERATOR3DNONUNIFORM,self).toString()       
        line += integerToSPF(self.Scale2)+','
        line += integerToSPF(self.Scale3)+','

        return line
