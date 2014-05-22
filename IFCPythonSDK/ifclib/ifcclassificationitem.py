#!/usr/bin/python
#coding=utf-8
#Filename:IfcClassificationItem.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCLASSIFICATIONITEM(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCLASSIFICATIONITEM,self).__init__(id,arg)
        self.type='IFCCLASSIFICATIONITEM'
        self.inverse={}
        self.Notation=None #IfcClassificationNotationFacet
        self.ItemOf=None #IfcClassification
        self.Title=None #IfcLabel
        self.inverse['IsClassifyingItemIn']=[] #inverse:SET of IfcClassificationItemRelationship
        self.inverse['IsClassifiedItemIn']=[] #inverse:SET of IfcClassificationItemRelationship


    def load(self):
        """register inverses"""
        if not super(IFCCLASSIFICATIONITEM,self).load():
            return False
        idx=super(IFCCLASSIFICATIONITEM,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcClassificationItem, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcClassificationItem, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCCLASSIFICATIONITEM','ItemOf',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCLASSIFICATIONITEM,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Notation= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ItemOf= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Title= fromSPF(arg)

        inverses = self.args.getInverses('IFCCLASSIFICATIONITEMRELATIONSHIP', 'RelatingItem');
        if inverses:
            self.inverse['IsClassifyingItemIn']=inverses

        inverses = self.args.getInverses('IFCCLASSIFICATIONITEMRELATIONSHIP', 'RelatedItems');
        if inverses:
            self.inverse['IsClassifiedItemIn']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCLASSIFICATIONITEM,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCCLASSIFICATIONITEM,self).toString()       
        line += idToSPF(self.Notation)+','
        line += idToSPF(self.ItemOf)+','
        line += strToSPF(self.Title)+','

        return line
