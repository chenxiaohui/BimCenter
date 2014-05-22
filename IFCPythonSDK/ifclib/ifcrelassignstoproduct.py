#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssignsToProduct.py
import log
import common
from ifcrelassigns import IFCRELASSIGNS

from utils import *

class IFCRELASSIGNSTOPRODUCT(IFCRELASSIGNS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSIGNSTOPRODUCT,self).__init__(id,arg)
        self.type='IFCRELASSIGNSTOPRODUCT'
        self.inverse={}
        self.RelatingProduct=None #IfcProduct


    def load(self):
        """register inverses"""
        if not super(IFCRELASSIGNSTOPRODUCT,self).load():
            return False
        idx=super(IFCRELASSIGNSTOPRODUCT,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToProduct, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToProduct, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELASSIGNSTOPRODUCT','RelatingProduct',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSIGNSTOPRODUCT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingProduct= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSIGNSTOPRODUCT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSIGNSTOPRODUCT,self).toString()       
        line += idToSPF(self.RelatingProduct)+','

        return line
