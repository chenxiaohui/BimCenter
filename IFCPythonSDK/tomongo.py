#!/usr/bin/python
#coding=utf-8
#Filename:tomongo.py
import config
import pymongo
def getConn():
    """"""
    conn=pymongo.Connection(config.get('mongo','host'),
                            int(config.get('mongo','port')))
    db=conn[config.get('mongo','database')]
    return conn,db

def toMongo(items,md5):
    """"""
    conn,db=getConn()
    cur=db[md5]
    if cur.count():#exists
        conn.close()
        return
    for key,value in items.items():
        document=value.toDict()
        document['id']=key
        cur.insert(document)
    conn.close()
        
        
if __name__ == '__main__':
    import log
    from utils import CalcMD5
    from spfreader import SPFReader

    log.InitLog()
    reader=SPFReader()
    filename="files/output.ifc"
    md5=CalcMD5(filename)   

    with file(filename,"r") as fp:
    #with file("files/room.ifc","r") as fp:
        reader.read(fp)
    expDataSet=reader.expDataSet
    expDataSet.instantiateAll()
    toMongo(expDataSet.Id2BaseObject,md5)
