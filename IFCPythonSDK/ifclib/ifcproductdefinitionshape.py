#!/usr/bin/python
#coding=utf-8
#Filename:IfcProductDefinitionShape.py
import log
import common
from ifcproductrepresentation import IFCPRODUCTREPRESENTATION

from utils import *

class IFCPRODUCTDEFINITIONSHAPE(IFCPRODUCTREPRESENTATION):
    """"""
    def __init__(self,id,arg):
        super(IFCPRODUCTDEFINITIONSHAPE,self).__init__(id,arg)
        self.type='IFCPRODUCTDEFINITIONSHAPE'
        self.inverse={}
        self.inverse['ShapeOfProduct']=[] #inverse:SET of IfcProduct
        self.inverse['HasShapeAspects']=[] #inverse:SET of IfcShapeAspect


    def load(self):
        """register inverses"""
        if not super(IFCPRODUCTDEFINITIONSHAPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPRODUCTDEFINITIONSHAPE,self).init():
            return False

        inverses = self.args.getInverses('IFCPRODUCT', 'Representation');
        if inverses:
            self.inverse['ShapeOfProduct']=inverses

        inverses = self.args.getInverses('IFCSHAPEASPECT', 'PartOfProductDefinitionShape');
        if inverses:
            self.inverse['HasShapeAspects']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPRODUCTDEFINITIONSHAPE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPRODUCTDEFINITIONSHAPE,self).toString()       

        return line
