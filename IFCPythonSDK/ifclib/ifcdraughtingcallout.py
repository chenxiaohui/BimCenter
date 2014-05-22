#!/usr/bin/python
#coding=utf-8
#Filename:IfcDraughtingCallout.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCDRAUGHTINGCALLOUT(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCDRAUGHTINGCALLOUT,self).__init__(id,arg)
        self.type='IFCDRAUGHTINGCALLOUT'
        self.inverse={}
        self.Contents=None #SET
        self.inverse['IsRelatedToCallout']=[] #inverse:SET of IfcDraughtingCalloutRelationship
        self.inverse['IsRelatedFromCallout']=[] #inverse:SET of IfcDraughtingCalloutRelationship


    def load(self):
        """register inverses"""
        if not super(IFCDRAUGHTINGCALLOUT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDRAUGHTINGCALLOUT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Contents= getIdListParam(arg,spfToTypeRef)

        inverses = self.args.getInverses('IFCDRAUGHTINGCALLOUTRELATIONSHIP', 'RelatingDraughtingCallout');
        if inverses:
            self.inverse['IsRelatedToCallout']=inverses

        inverses = self.args.getInverses('IFCDRAUGHTINGCALLOUTRELATIONSHIP', 'RelatedDraughtingCallout');
        if inverses:
            self.inverse['IsRelatedFromCallout']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDRAUGHTINGCALLOUT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCDRAUGHTINGCALLOUT,self).toString()       
        line += listParamToSPF(self.Contents,typerefToSPF)+','

        return line
