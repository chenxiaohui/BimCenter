#!/usr/bin/python
#coding=utf-8
#Filename:IfcRepresentationContext.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCREPRESENTATIONCONTEXT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCREPRESENTATIONCONTEXT,self).__init__(id,arg)
        self.type='IFCREPRESENTATIONCONTEXT'
        self.inverse={}
        self.ContextIdentifier=None #IfcLabel
        self.ContextType=None #IfcLabel
        self.inverse['RepresentationsInContext']=[] #inverse:SET of IfcRepresentation


    def load(self):
        """register inverses"""
        if not super(IFCREPRESENTATIONCONTEXT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREPRESENTATIONCONTEXT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ContextIdentifier= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ContextType= fromSPF(arg)

        inverses = self.args.getInverses('IFCREPRESENTATION', 'ContextOfItems');
        if inverses:
            self.inverse['RepresentationsInContext']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREPRESENTATIONCONTEXT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCREPRESENTATIONCONTEXT,self).toString()       
        line += strToSPF(self.ContextIdentifier)+','
        line += strToSPF(self.ContextType)+','

        return line
