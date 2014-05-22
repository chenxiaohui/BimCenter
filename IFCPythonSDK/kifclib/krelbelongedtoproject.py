#!/usr/bin/python
#coding=utf-8
#Filename:KRelBelongedToProject.py
import log
import common
from krelation import KRELATION

from utils import *

class KRELBELONGEDTOPROJECT(KRELATION):
    """"""
    def __init__(self,id,arg):
        super(KRELBELONGEDTOPROJECT,self).__init__(id,arg)
        self.type='KRELBELONGEDTOPROJECT'
        self.inverse={}
        self.Documents=[] #SET
        self.Owner=None #KProject


    def load(self):
        """register inverses"""
        if not super(KRELBELONGEDTOPROJECT,self).load():
            return False
        idx=super(KRELBELONGEDTOPROJECT,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of KRelBelongedToProject, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList[0]==ID_UNDEF:
            log.error("Inverse links : Error during reading parameter 0 of KRelBelongedToProject, line %d"%common.counter)
            return False
        if currentRefList[0]!=ID_UNSET:
            for i in currentRefList:
                self.expDataSet.getArgs(i).addInverse('KRELBELONGEDTOPROJECT','Documents',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of KRelBelongedToProject, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList[0]==ID_UNDEF:
            log.error("Inverse links : Error during reading parameter 1 of KRelBelongedToProject, line %d"%common.counter)
            return False
        if currentRefList[0]!=ID_UNSET:
            for i in currentRefList:
                self.expDataSet.getArgs(i).addInverse('KRELBELONGEDTOPROJECT','Owner',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(KRELBELONGEDTOPROJECT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Documents= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Owner= spfToId(arg)

        return True

    def getAttrCount(self):
        """"""
        return super(KRELBELONGEDTOPROJECT,self).getAttrCount()+2
