#!/usr/bin/python
#coding=utf-8
#Filename:tomysql.py
import config
import log
import MySQLdb as mdb
import pymongo
#from DBUtils.PooledDB import PooledDB

conn,cur=None,None
monConn,db=None,None

def getMongoConn():
    """"""
    conn=pymongo.Connection(config.get('mongo','host'),
                            int(config.get('mongo','port')))
    db=conn[config.get('mongo','database')]
    return conn,db

def getMysqlConn():
    """init connection to mysql 
    """
    try:
        conn=mdb.connect(
                        host=config.get('mysql','host'),\
                        db=config.get('mysql','database'),\
                        user=config.get('mysql','user'),\
                        passwd=config.get('mysql','passwd'))
        cur=conn.cursor(mdb.cursors.Cursor)
        return conn,cur
    except Exception , e:
        raise e

def InitConn():
    """"""
    global conn,cur,monConn,db
    conn,cur=getMysqlConn()
    monConn,db=getMongoConn()
    
def Close():
    """"""
    cur.close()
    conn.close()
    monConn.close()
       
#dbpool=None
#def InitConn():
    #"""init connection to mysql 
    #"""
    #try:
        #global dbpool
        #dbpool=PooledDB(creator=mdb,\
                        #maxusage=int(config.get('db','max_usage')),\
                        #host=config.get('db','host'),\
                        #db=config.get('db','database'),\
                        #user=config.get('db','user'),
                        #passwd=config.get('db','passwd'))
        #print 'DBPool init succeed.'
    #except Exception , e:
        #raise e

#def getConn():
    #""""""
    #conn=dbpool.connection()
    #cur=conn.cursor(mdb.cursors.DictCursor)
    #return conn,cur

def toMySQL(model,dataset,hash,model_id=None,increment=False):
    """
        model_id:model serial number
        do not has model_id: a new model
        if has model_id:  a new version
        if  increment: increment model
        not increment: full model
    """

    InitConn()
    #does not change
    if cur.execute('select version,id from sdk_indexes where hash=%s',hash):
        version=cur.fetchone()[0]
        Close()
        return 'version has exists,model_id:%s,version_id:%s,hash:%s'%(model_id,version,hash)

    #create table
    if cur.execute("show tables like '%s'"%hash):
        cur.execute(" DROP TABLE IF EXISTS `%s`; "%hash)
        conn.commit()

    cur.execute("Create table `%s` ( `id` int(11) NOT NULL DEFAULT '0', `name` varchar(100) DEFAULT NULL, `param` TEXT DEFAULT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8; "%hash)
    conn.commit()

    header=dataset.header
    fileDesc=header.fileDescription
    fileName=header.fileName
    fileSchema=header.fileSchema
    #new model
    if not model_id:
        cur.execute('select max(model_id) from sdk_indexes')
        try:
            maxModelId=int(cur.fetchone()[0])
        except Exception:
            maxModelId=0

        insertMagnanimity(model,dataset,hash)
        #get a new id
        cur.execute("insert into sdk_indexes(`hash`, `version`, `model_id` , `description` , `implementationLevel` , `name`, `author` , `organization` , `preprocessorVersion` , `originatingSystem` , `authorization` , `schemaIdentifiers`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [hash,'1',str(maxModelId+1)]+fileDesc.toDict()+fileName.toDict()+fileSchema.toDict())
        conn.commit()
    #model exists
    else:
        cur.execute('select max(version) from sdk_indexes where model_id=%d'% model_id)
        try:
            maxVersion=float(cur.fetchone()[0])
        except Exception:
            maxVersion=0

        #if increment:#increment model
            #insertIncrement(model,dataset,hash,model_id,maxVersion)
        #else:
            #insertMagnanimity(model,dataset,hash)
        insertMagnanimity(model,dataset,hash)

        #versionIncrease=0.1 if increment else 1
        versionIncrease= 1

        cur.execute("insert into sdk_indexes(`hash`, `version`, `model_id` , `description` , `implementationLevel` , `name`, `author` , `organization` , `preprocessorVersion` , `originatingSystem` , `authorization` , `schemaIdentifiers` ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [hash,str(maxVersion+versionIncrease),model_id]+fileDesc.toDict()+fileName.toDict()+fileSchema.toDict())
        conn.commit()
    
    cur.execute('create index nameIndex on %s(name)'%hash)
    conn.commit()

    col=db[hash]
    col.create_index('id')
    col.create_index('type')

    Close()
    return hash

def applyPatches(version,model_id):
    """"""
    #copy of basetable
    cur.execute("select hash from sdk_indexes where model_id=%d and version=%.1f"%(model_id,version))
    tableName=cur.fetchone()[0]

    #ids to update
    cur.execute('select id,name,param from %s where id<0'%tableName)
    recsToUpdate=cur.fetchall()
    for rec in recsToUpdate:
        cur.execute("update temp set name=%s,param=%s where id=%s",(rec[1],rec[2],str(-rec[0])))
    conn.commit()

    #delete 
    cur.execute('select param from %s where id=0'%tableName)
    idsToDel=cur.fetchone()
    if idsToDel:
        cur.execute('delete from temp where id in (%s)'%idsToDel[0])
        conn.commit()

    #insert
    cur.execute("insert into temp (select id,name,param from %s where id>0)"%tableName)
    conn.commit()
    

#def insertIncrement(model,dataset,hash,model_id,maxVersion):
    #""" add increment model
    #"""
    #baseVersion=int(maxVersion)
    #print 'baseVersion=%.1f maxVersion=%.1f'%( maxVersion,baseVersion )

    ##copy of basetable
    #cur.execute('select hash from sdk_indexes where model_id=%d and version=%f'%(model_id,baseVersion))
    #baseHash=cur.fetchone()[0]
    #cur.execute('truncate temp')
    #cur.execute('insert into temp (select id,name,param from `%s`)'%baseHash)
    #conn.commit()

    ##apply changes
    #while baseVersion<maxVersion:
        #baseVersion+=0.1
        #applyPatches(baseVersion,model_id)
    
    ##get new patch
    #cur.execute('select id from temp')
    #baseIds=[s[0] for s in cur.fetchall()]
    #ids=[]
    #values=[]
    #idsToDel=[]
    #for i in baseIds:
        #if i not in model.lines: #del
            #idsToDel.append(str(i))
        #else:#modify
            #cur.execute('select name,param from temp where id=%d'%i)
            #name,param=cur.fetchone()
            #line=model.lines[i]
            #if name!=line[0] or param!=line[1]:
                #values.append([str(-i),line[0],line[1]])       
                #ids.append(i)
            #del model.lines[i]
    #col=db[hash]
    ##update
    #if values:
        #cur.executemany('insert into `'+hash+'` values(%s,%s,%s)',values)
        #conn.commit()
        #for i in ids:
            #document=dataset.Id2BaseObject[i].toDict()
            #document['id']=-i
            #col.insert(document)
    ##delete
    #if idsToDel:
        #idsString=','.join(idsToDel)
        #cur.execute("insert into %s(id,param) values(0,'%s')"%(hash,idsString))
        #conn.commit()
        #col.insert({'id':0,'delete':idsString})

    ##add
    #values=[]
    #ids=[]
    #for lid,line in model.lines.items():
        #values.append([str(lid),line[0],line[1]])       
        #ids.append(lid)
    #if values:
        #cur.executemany('insert into `'+hash+'` values(%s,%s,%s)',values)
        #conn.commit()
        #for i in ids:
            #document=dataset.Id2BaseObject[i].toDict()
            #document['id']=i
            #col.insert(document)
    
def insertMagnanimity(model,dataset,hash):
    """"""
    values=[]
    for lid,line in model.lines.items():
        values.append([str(lid),line[0],line[1]])       
        if len(values)==100:
            cur.executemany('insert into `'+hash+'` values(%s,%s,%s)',values)
            conn.commit()
            values=[]

    if values:
            cur.executemany('insert into `'+hash+'` values(%s,%s,%s)',values)
            conn.commit()
    
    col=db[hash]
    for key,value in dataset.Id2BaseObject.items():
        document=value.toDict()
        document['id']=key
        col.insert(document)

def deleteVersion(model_id,version=None):
    """"""
    #indexes
    InitConn()
    if version:
        if not cur.execute('select id,hash from sdk_indexes where model_id=%d and version=%.1f'%(model_id,version)):
            Close()
            return
        id,hash=cur.fetchone()
        cur.execute('delete from sdk_indexes where id=%d'%id)
        conn.commit()
        #MySQL
        if cur.execute("show tables like '%s'"%hash):
            cur.execute(" DROP TABLE IF EXISTS `%s`; "%hash)
            conn.commit()
        #mongo
        col=db[hash]
        col.drop()
    else:
        if not cur.execute('select id,hash from sdk_indexes where model_id=%d'%model_id):
            Close()
            return
        for id,hash in cur.fetchall():
            cur.execute('delete from sdk_indexes where id=%d'%id)
            conn.commit()
            #MySQL
            if cur.execute("show tables like '%s'"%hash):
                cur.execute(" DROP TABLE IF EXISTS `%s`; "%hash)
                conn.commit()
            #mongo
            col=db[hash]
            col.drop()
    Close()
     
def getFullVersion(model_id,version_id):
    """ get a full version
        if version_id is full, return it's hash
        else calculate the full version and retrun 'temp'
    """
    baseVersion=int(version_id)
    print 'baseVersion=%.1f maxVersion=%.1f'%(version_id ,baseVersion )
    if version_id==baseVersion:#full version
        cur.execute('select hash from sdk_indexes where model_id=%d and version=%f'%(model_id,baseVersion))
        currentHash=cur.fetchone()[0]
        return currentHash

    #copy of basetable
    cur.execute('select hash from sdk_indexes where model_id=%d and version=%f'%(model_id,baseVersion))
    baseHash=cur.fetchone()[0]
    cur.execute('truncate temp')
    cur.execute('insert into temp (select id,name,param from `%s`)'%baseHash)
    conn.commit()

    #apply changes
    while baseVersion<version_id:
        baseVersion+=0.1
        applyPatches(baseVersion,model_id)
    #get a full version in the temp
    return 'temp'

if __name__ == '__main__':
    from submodel import SubModel
    from spfreader import SPFReader
    from utils import CalcMD5
    log.InitLog()
    
    #deleteVersion(1)

    #filename="files/ceshi.ifc"
    filename="files/Module_8_Drawing_With_Base_Quantities.ifc"
    hash=CalcMD5(filename)   

    reader=SPFReader()
    with file(filename,"r") as fp:
        reader.read(fp)
    expDataSet=reader.expDataSet
    expDataSet.instantiateAll()

    model=SubModel()
    with open(filename,'r') as fp:
        model.read(fp)

    print toMySQL(model,expDataSet,hash,1)

