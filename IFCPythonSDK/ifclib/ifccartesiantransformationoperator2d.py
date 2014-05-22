#!/usr/bin/python
#coding=utf-8
#Filename:IfcCartesianTransformationOperator2D.py
import log
import common
from ifccartesiantransformationoperator import IFCCARTESIANTRANSFORMATIONOPERATOR

from utils import *

class IFCCARTESIANTRANSFORMATIONOPERATOR2D(IFCCARTESIANTRANSFORMATIONOPERATOR):
    """"""
    def __init__(self,id,arg):
        super(IFCCARTESIANTRANSFORMATIONOPERATOR2D,self).__init__(id,arg)
        self.type='IFCCARTESIANTRANSFORMATIONOPERATOR2D'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCCARTESIANTRANSFORMATIONOPERATOR2D,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCARTESIANTRANSFORMATIONOPERATOR2D,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCARTESIANTRANSFORMATIONOPERATOR2D,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCARTESIANTRANSFORMATIONOPERATOR2D,self).toString()       

        return line
