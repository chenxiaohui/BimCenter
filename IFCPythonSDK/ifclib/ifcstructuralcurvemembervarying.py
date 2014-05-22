#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralCurveMemberVarying.py
import log
import common
from ifcstructuralcurvemember import IFCSTRUCTURALCURVEMEMBER

from utils import *

class IFCSTRUCTURALCURVEMEMBERVARYING(IFCSTRUCTURALCURVEMEMBER):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALCURVEMEMBERVARYING,self).__init__(id,arg)
        self.type='IFCSTRUCTURALCURVEMEMBERVARYING'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALCURVEMEMBERVARYING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALCURVEMEMBERVARYING,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALCURVEMEMBERVARYING,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALCURVEMEMBERVARYING,self).toString()       

        return line
