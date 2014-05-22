#!/usr/bin/python
#coding=utf-8
#Filename:test.py
import log
from ifclib import *
from utils import CalcMD5
import config
import pymongo
import json
from spfreader import SPFReader
from tojson import toJson
from toifc import toIFC

def getConn():
    """"""
    conn=pymongo.Connection(config.get('mongo','host'),
                            int(config.get('mongo','port')))
    db=conn[config.get('mongo','database')]
    return conn,db

def pprint(obj):
    """"""
    print json.dumps(obj,indent=4)

def query(condition):
    """"""
    return col.find_one(condition,{'_id':0})

#consumption
#hash='193ab02b353e9d3a59d719c87ffbdc52'
#conn,db=getConn()
#col=db[hash]
def idToSPF(idx):
    """"""
    if not idx:
        return '$'
    return '#%d'%idx
def strToSPF(string):
    """"""
    if not string:
        return '$'
    return "'%s'"%string


def listParamToSPF(args,func=idToSPF):
    """"""
    if not args:
        return '$'
    params=['%s'%func(i) for i in args]
    return '(%s)'%(','.join(params))

    
if __name__ == '__main__':
    #pprint(query({'type':'IFCORGANIZATION'}))
    #metadata=query({'id':1})
    #ob=IFCORGANIZATION(1,'')
    #for key,value in metadata.items():
        #ob.__dict__[key]=value
    #pprint(ob.__dict__)
    #st=''
    #with open('test.txt','r') as fp:
        #c=fp.read(1)
        #while c:
            #st+=c
            #c=fp.read(1)
    
    #print json.dumps({'name':st.decode('utf-8')},ensure_ascii=False)

    #import pyxser as pyx


    #ser = pyx.serialize(obj={'a':1,'b':1}, enc="utf-8")
    #print(ser)
    #import dict2xml
    #print dict2xml.dict2Xml({'a':1},'')

    log.InitLog()
    reader=SPFReader()
    filename="files/2floor.ifc"
    md5=CalcMD5(filename)   
    with open(filename,"r") as fp:
        reader.read(fp)
    expDataSet=reader.expDataSet
    expDataSet.instantiateAll()
    #toJson(expDataSet.Id2BaseObject,md5)
    toIFC(expDataSet.header,expDataSet.Id2BaseObject,'files/2floorout.ifc') 


    #fp=open("line.json",'r')
    #metadata=json.load(fp)
    #pprint (metadata)
    #ob=IFCSLAB(284,'')
    #for key,value in metadata.items():
        #ob.__dict__[key]=value
    ##pprint (ob.toDict())
    #print ob.toCode()
        
