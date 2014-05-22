#!/usr/bin/python
#coding=utf-8
#Filename:__init__.py

import log
from utils import CalcMD5
from submodel import SubModel
from tojson import toJson
from tomongo import toMongo
from tograph import toGraph
from tomysql import toMySQL,deleteVersion
from spfreader import SPFReader
from srlparser import getSubModel
from tobsd import toBsd

def toXml(items,append=False):
    """"""
    for key,value in items.items():
        fp.write(str(key).center(70,'*')+'\n')
        fp.write(value.Serialize()+'\n')

if __name__ == '__main__':
    log.InitLog()
    reader=SPFReader()
    #filename="test.kfc"
    #filename="files/Module_8_Drawing_With_Base_Quantities.ifc"
    filename="files/room.ifc"
    md5=CalcMD5(filename)   

    with open(filename,"r") as fp:
        reader.read(fp)
    expDataSet=reader.expDataSet
    expDataSet.instantiateAll()

    #model=SubModel()
    #with open(filename,'r') as fp:
        #model.read(fp)
    
    toJson(expDataSet.Id2BaseObject,md5)
    #toBsd(expDataSet.Id2BaseObject,md5)
    #toMongo(expDataSet.Id2BaseObject,md5)
    #toGraph(model,md5)
    #toMySQL(model,md5)
    

