#!/usr/bin/python
#coding=utf-8
#Filename:IfcPhysicalComplexQuantity.py
import log
import common
from ifcphysicalquantity import IFCPHYSICALQUANTITY

from utils import *

class IFCPHYSICALCOMPLEXQUANTITY(IFCPHYSICALQUANTITY):
    """"""
    def __init__(self,id,arg):
        super(IFCPHYSICALCOMPLEXQUANTITY,self).__init__(id,arg)
        self.type='IFCPHYSICALCOMPLEXQUANTITY'
        self.inverse={}
        self.HasQuantities=None #SET
        self.Discrimination=None #IfcLabel
        self.Quality=None #IfcLabel
        self.Usage=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCPHYSICALCOMPLEXQUANTITY,self).load():
            return False
        idx=super(IFCPHYSICALCOMPLEXQUANTITY,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcPhysicalComplexQuantity, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcPhysicalComplexQuantity, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCPHYSICALCOMPLEXQUANTITY','HasQuantities',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPHYSICALCOMPLEXQUANTITY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HasQuantities= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Discrimination= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Quality= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Usage= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPHYSICALCOMPLEXQUANTITY,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCPHYSICALCOMPLEXQUANTITY,self).toString()       
        line += listParamToSPF(self.HasQuantities,idToSPF)+','
        line += strToSPF(self.Discrimination)+','
        line += strToSPF(self.Quality)+','
        line += strToSPF(self.Usage)+','

        return line
