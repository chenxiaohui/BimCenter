#!/usr/bin/python
#coding=utf-8
#Filename:ExpressDataSet.py
from spfdata import SPFData
from spfheader import SPFHeader
from baseobject import BaseObject
from ifclib import *
from kifclib import *

class ExpressDataSet(object):
    """"""
    def __init__(self):
        super(ExpressDataSet,self).__init__()
        self.header=SPFHeader()
        self.maxId=0
        self.Id2BaseObject={}

    def getSPFObject(self,id,type=None):
        """"""
        if not id in self.Id2BaseObject:
            #create new object
            self.updateMaxId(id)
            cmd='%s(%d,SPFData())'%(type.upper(),id)
            obj=eval(cmd)
            obj.expDataSet=self
            self.Id2BaseObject[id]=obj
            return obj
        else:
            obj=self.Id2BaseObject[id]
            if obj.type:
                #real object
                return obj 
            else:
                #pre created object
                cmd='%s(%d,obj.args)'%(type.upper(),id)
                newobj=eval(cmd)
                newobj.expDataSet=self
                self.Id2BaseObject[id]=newobj
                return newobj

    def getArgs(self,id):
        """return empty object
        """
        if not id in self.Id2BaseObject:
            self.updateMaxId(id)
            obj=BaseObject(id,SPFData())
            obj.expDataSet=self
            self.Id2BaseObject[id]=obj
            return obj.args
        else:
            return self.Id2BaseObject[id].args

    def updateMaxId(self,id):
        """"""
        if id>self.maxId:
            self.maxId=id

    def getNewId(self):
        """"""
        self.maxId+=1
        return self.maxId
    
    def setHeader(self,header):
        """"""
        self.header=header
        
    #def allocate(self,Type,id):
        #""""""
        #if id==0:
            #id=self.getNewId()
            #arg=SPFData()
        #else:
            #arg=self.args
        #ret=Type(id,arg)
        ##self.registerObject(id,ret)
        #return ret

    def instantiateAll(self):
        """"""
        for (key,val) in self.Id2BaseObject.items():
                val.inited()
        
