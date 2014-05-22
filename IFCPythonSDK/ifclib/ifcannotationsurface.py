#!/usr/bin/python
#coding=utf-8
#Filename:IfcAnnotationSurface.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCANNOTATIONSURFACE(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCANNOTATIONSURFACE,self).__init__(id,arg)
        self.type='IFCANNOTATIONSURFACE'
        self.inverse={}
        self.Item=None #IfcGeometricRepresentationItem
        self.TextureCoordinates=None #IfcTextureCoordinate


    def load(self):
        """register inverses"""
        if not super(IFCANNOTATIONSURFACE,self).load():
            return False
        idx=super(IFCANNOTATIONSURFACE,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcAnnotationSurface, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcAnnotationSurface, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCANNOTATIONSURFACE','TextureCoordinates',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCANNOTATIONSURFACE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Item= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TextureCoordinates= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCANNOTATIONSURFACE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCANNOTATIONSURFACE,self).toString()       
        line += idToSPF(self.Item)+','
        line += idToSPF(self.TextureCoordinates)+','

        return line
