#!/usr/bin/python
#coding=utf-8
#Filename:IfcProduct.py
import log
import common
from ifcobject import IFCOBJECT

from utils import *

class IFCPRODUCT(IFCOBJECT):
    """"""
    def __init__(self,id,arg):
        super(IFCPRODUCT,self).__init__(id,arg)
        self.type='IFCPRODUCT'
        self.inverse={}
        self.ObjectPlacement=None #IfcObjectPlacement
        self.Representation=None #IfcProductRepresentation
        self.inverse['ReferencedBy']=[] #inverse:SET of IfcRelAssignsToProduct


    def load(self):
        """register inverses"""
        if not super(IFCPRODUCT,self).load():
            return False
        idx=super(IFCPRODUCT,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcProduct, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcProduct, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCPRODUCT','ObjectPlacement',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcProduct, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcProduct, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCPRODUCT','Representation',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPRODUCT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ObjectPlacement= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Representation= spfToId(arg)

        inverses = self.args.getInverses('IFCRELASSIGNSTOPRODUCT', 'RelatingProduct');
        if inverses:
            self.inverse['ReferencedBy']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPRODUCT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPRODUCT,self).toString()       
        line += idToSPF(self.ObjectPlacement)+','
        line += idToSPF(self.Representation)+','

        return line
