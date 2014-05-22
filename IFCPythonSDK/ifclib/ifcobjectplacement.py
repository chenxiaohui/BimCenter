#!/usr/bin/python
#coding=utf-8
#Filename:IfcObjectPlacement.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCOBJECTPLACEMENT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCOBJECTPLACEMENT,self).__init__(id,arg)
        self.type='IFCOBJECTPLACEMENT'
        self.inverse={}
        self.inverse['PlacesObject']=[] #inverse:SET of IfcProduct
        self.inverse['ReferencedByPlacements']=[] #inverse:SET of IfcLocalPlacement


    def load(self):
        """register inverses"""
        if not super(IFCOBJECTPLACEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCOBJECTPLACEMENT,self).init():
            return False

        inverses = self.args.getInverses('IFCPRODUCT', 'ObjectPlacement');
        if inverses:
            self.inverse['PlacesObject']=inverses

        inverses = self.args.getInverses('IFCLOCALPLACEMENT', 'PlacementRelTo');
        if inverses:
            self.inverse['ReferencedByPlacements']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCOBJECTPLACEMENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCOBJECTPLACEMENT,self).toString()       

        return line
