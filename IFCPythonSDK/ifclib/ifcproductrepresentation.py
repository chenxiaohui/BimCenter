#!/usr/bin/python
#coding=utf-8
#Filename:IfcProductRepresentation.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPRODUCTREPRESENTATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPRODUCTREPRESENTATION,self).__init__(id,arg)
        self.type='IFCPRODUCTREPRESENTATION'
        self.inverse={}
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.Representations=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCPRODUCTREPRESENTATION,self).load():
            return False
        idx=super(IFCPRODUCTREPRESENTATION,self).getAttrCount()
        if self.args.argc()<=idx+2:
            log.error("Inverse links : Error during reading parameter 2 of IfcProductRepresentation, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+2])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 2 of IfcProductRepresentation, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCPRODUCTREPRESENTATION','Representations',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPRODUCTREPRESENTATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Representations= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPRODUCTREPRESENTATION,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCPRODUCTREPRESENTATION,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += listParamToSPF(self.Representations,idToSPF)+','

        return line
