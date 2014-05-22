#!/usr/bin/python
#coding=utf-8
#Filename:IfcShapeModel.py
import log
import common
from ifcrepresentation import IFCREPRESENTATION

from utils import *

class IFCSHAPEMODEL(IFCREPRESENTATION):
    """"""
    def __init__(self,id,arg):
        super(IFCSHAPEMODEL,self).__init__(id,arg)
        self.type='IFCSHAPEMODEL'
        self.inverse={}
        self.inverse['OfShapeAspect']=[] #inverse:SET of IfcShapeAspect


    def load(self):
        """register inverses"""
        if not super(IFCSHAPEMODEL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSHAPEMODEL,self).init():
            return False

        inverses = self.args.getInverses('IFCSHAPEASPECT', 'ShapeRepresentations');
        if inverses:
            self.inverse['OfShapeAspect']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSHAPEMODEL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSHAPEMODEL,self).toString()       

        return line
