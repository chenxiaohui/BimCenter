#!/usr/bin/python
#coding=utf-8
#Filename:IfcFeatureElementSubtraction.py
import log
import common
from ifcfeatureelement import IFCFEATUREELEMENT

from utils import *

class IFCFEATUREELEMENTSUBTRACTION(IFCFEATUREELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCFEATUREELEMENTSUBTRACTION,self).__init__(id,arg)
        self.type='IFCFEATUREELEMENTSUBTRACTION'
        self.inverse={}
        self.inverse['VoidsElements']=[] #inverse:IfcRelVoidsElement of Alone


    def load(self):
        """register inverses"""
        if not super(IFCFEATUREELEMENTSUBTRACTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFEATUREELEMENTSUBTRACTION,self).init():
            return False

        inverses = self.args.getInverses('IFCRELVOIDSELEMENT', 'RelatedOpeningElement');
        if inverses:
            self.inverse['VoidsElements']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFEATUREELEMENTSUBTRACTION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCFEATUREELEMENTSUBTRACTION,self).toString()       

        return line
