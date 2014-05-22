#!/usr/bin/python
#coding=utf-8
#Filename:IfcObject.py
import log
import common
from ifcobjectdefinition import IFCOBJECTDEFINITION

from utils import *

class IFCOBJECT(IFCOBJECTDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCOBJECT,self).__init__(id,arg)
        self.type='IFCOBJECT'
        self.inverse={}
        self.ObjectType=None #IfcLabel
        self.inverse['IsDefinedBy']=[] #inverse:SET of IfcRelDefines


    def load(self):
        """register inverses"""
        if not super(IFCOBJECT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCOBJECT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ObjectType= fromSPF(arg)

        inverses = self.args.getInverses('IFCRELDEFINES', 'RelatedObjects');
        if inverses:
            self.inverse['IsDefinedBy']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCOBJECT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCOBJECT,self).toString()       
        line += strToSPF(self.ObjectType)+','

        return line
