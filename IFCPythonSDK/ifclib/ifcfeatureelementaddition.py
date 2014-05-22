#!/usr/bin/python
#coding=utf-8
#Filename:IfcFeatureElementAddition.py
import log
import common
from ifcfeatureelement import IFCFEATUREELEMENT

from utils import *

class IFCFEATUREELEMENTADDITION(IFCFEATUREELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFEATUREELEMENTADDITION,self).__init__(id,arg)
        self.type='IFCFEATUREELEMENTADDITION'
        self.inverse={}
        self.inverse['ProjectsElements']=[] #inverse:IfcRelProjectsElement of Alone


    def load(self):
        """register inverses"""
        if not super(IFCFEATUREELEMENTADDITION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFEATUREELEMENTADDITION,self).init():
            return False

        inverses = self.args.getInverses('IFCRELPROJECTSELEMENT', 'RelatedFeatureElement');
        if inverses:
            self.inverse['ProjectsElements']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFEATUREELEMENTADDITION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFEATUREELEMENTADDITION,self).toString()       

        return line
