#!/usr/bin/python
#coding=utf-8
#Filename:IfcRepresentationItem.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCREPRESENTATIONITEM(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCREPRESENTATIONITEM,self).__init__(id,arg)
        self.type='IFCREPRESENTATIONITEM'
        self.inverse={}
        self.inverse['LayerAssignments']=[] #inverse:SET of IfcPresentationLayerAssignment
        self.inverse['StyledByItem']=[] #inverse:SET of IfcStyledItem


    def load(self):
        """register inverses"""
        if not super(IFCREPRESENTATIONITEM,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREPRESENTATIONITEM,self).init():
            return False

        inverses = self.args.getInverses('IFCPRESENTATIONLAYERASSIGNMENT', 'AssignedItems');
        if inverses:
            self.inverse['LayerAssignments']=inverses

        inverses = self.args.getInverses('IFCSTYLEDITEM', 'Item');
        if inverses:
            self.inverse['StyledByItem']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREPRESENTATIONITEM,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCREPRESENTATIONITEM,self).toString()       

        return line
