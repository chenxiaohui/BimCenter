#!/usr/bin/python
#coding=utf-8
#Filename:IfcShapeAspect.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCSHAPEASPECT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCSHAPEASPECT,self).__init__(id,arg)
        self.type='IFCSHAPEASPECT'
        self.inverse={}
        self.ShapeRepresentations=None #LIST
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.ProductDefinitional=None #LOGICAL
        self.PartOfProductDefinitionShape=None #IfcProductDefinitionShape


    def load(self):
        """register inverses"""
        if not super(IFCSHAPEASPECT,self).load():
            return False
        idx=super(IFCSHAPEASPECT,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcShapeAspect, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcShapeAspect, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCSHAPEASPECT','ShapeRepresentations',self.lid)
        if self.args.argc()<=idx+4:
            log.error("Inverse links : Error during reading parameter 4 of IfcShapeAspect, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+4])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 4 of IfcShapeAspect, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCSHAPEASPECT','PartOfProductDefinitionShape',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSHAPEASPECT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShapeRepresentations= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProductDefinitional= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PartOfProductDefinitionShape= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSHAPEASPECT,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCSHAPEASPECT,self).toString()       
        line += listParamToSPF(self.ShapeRepresentations,idToSPF)+','
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += logicalToSPF(self.ProductDefinitional)+','
        line += idToSPF(self.PartOfProductDefinitionShape)+','

        return line
