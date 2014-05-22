#!/usr/bin/python
#coding=utf-8
#Filename:srlparser.py
import re
from utils import render
from expressionparser import ExpressionParser
from tomysql import getMysqlConn,getMongoConn
from BitVector import BitVector

md5=''
subids=list()
bitmap=None
pattern=re.compile(r'#(\d+)')
conn,cur=None,None
monConn,db=None,None

class node(object):
    """"""
    def __init__(self,name):
        super(node,self).__init__()
        self.name=name
        self.attr=[]
        self.where=[]

    def add(self,attr):
        """"""
        self.attr.append(attr)

    def dump(self,level=0):
        """"""
        print '    '*level,
        print self.name,
        print self.where if self.where else ''
        for i in self.attr:
            i.dump(level+1)

    def __repr__(self):
        return self.name+' '+str(self.where)
    
    def __str__(self):
        return self.name+' '+str(self.where)
    
       
def parseSRL(filename):
    """"""
    nodes=[]

    blockCommentPattern=re.compile(r'/\*[\s\S]*\*/')
    lineCommentPattern=re.compile(r'//.*\n')

    with open(filename,'r') as fp:
        fileContent=fp.read()
        fileContent=blockCommentPattern.sub('',fileContent)
        lines=lineCommentPattern.sub('',fileContent).split('\n')

        for line in lines:
            if not line:
                continue

            line=line.strip('\r\n').replace('    ','\t').strip(' ')

            if not line:
                continue

            idx=0
            while line[idx]=='\t':
                idx+=1
            attrname=line[idx:]
            pos=attrname.find('where')
            where=[]
            if pos>=0:
                whereClause=attrname[pos+5:].strip(' ')
                exp=ExpressionParser(whereClause)
                where=exp.parse()
                attrname=attrname[:pos].strip(' ')
            #print idx, attrname
        
            n=node(attrname)
            if where:
                n.where=where
            #parse
            if idx==0:#top entities
                nodes.append(n)
                level=idx #last level
                lastnode=n
                stack=[]
            elif idx==level:#new brother
                stack[-1].add(n)  
            elif idx>level:#new attr
                stack.append(lastnode)
                stack[-1].add(n)  
            else: #pop stack
                while level>idx:
                    stack.pop()
                    level-=1
                stack[-1].add(n)
            level=idx
            lastnode=n

    return nodes

def getMaxId():
    """"""
    sql='select max(id) from %s';
    cur.execute(sql%md5)
    return int(cur.fetchone()[0])

def setBits(ids):
    """"""
    global bitmap
    for id in ids:
        bitmap[id]=1

def visitEntities(entities):
    """"""
    global bitmap
    bitmap=BitVector(size=getMaxId()+1)
    for entity in entities:
        #visit current entity
        ids=nameToIds(entity.name,entity.where)
        #print nametoids(ifcdoor->(#234,#342))
        setBits(ids)

        if entity.attr:#has attr
            extractAttr(entity.attr,ids)
        else:
            #no attribute rules
            extractSubItems(ids)

def extractAttr(attrs,ids):
    """ extract this attr on all ids
        attrs: attr desc of this kind
        ids:   ids of same kind
    """ 
    for id in ids:
        #get id->entity
        entity= getEntity(id)
        #vlidate expression condition
        #id or id list
        for attr in attrs:
            refs=set()
            ref=entity[attr.name]
            if isinstance(ref,list):
                if attr.where:
                    for i in ref:
                        if validateExp(getEntity(i),attr.where):
                            refs.add(i)
                else:
                    refs.update(ref)
            else:
                if attr.where:
                    if validateExp(getEntity(ref),attr.where):
                        refs.add(ref)
                else:
                    refs.add(ref)

            print id,attr.name, ref

            setBits(refs)
            if attr.attr: #has sub attr
                #get every entity's attr ref id ->4,5,6
                extractAttr(attr.attr,refs)
            else:#append
                extractSubItems(refs)

def extractSubItems(ids):
    """"""
    currentIds=list(ids)
    while currentIds:
        curId=currentIds.pop(0)#get current
        params=getParam(curId)
        refs=pattern.findall(params)
        for ref in refs:
            ref=int(ref)
            if not bitmap[ref]:
                currentIds.append(ref)
                bitmap[ref]=1
            

def generateModelFile(to=None):
    """"""
    code=''
    lines=getLines()
    for line in lines:
        code+='#%d=%s(%s);\n'%(line[0],line[1],line[2])

    if cur.execute('select description , implementationLevel , name , author, organization , preprocessorVersion, originatingSystem,authorization, schemaIdentifiers from sdk_indexes where hash=%s',md5):
        #print cur.fetchone()
        idx=cur.fetchone()
        return render('temp.ifc',
               {
                    'description':idx[0],
                    'implementationLevel':idx[1],
                    'name' :idx[2],
                    'author':idx[3],
                    'organization':idx[4],
                    'preprocessorVersion':idx[5],
                    'originatingSystem':idx[6],
                    'authorization':idx[7],
                    'schemaIdentifiers':idx[8],
                    'data':code
               },
              to)


def validateExp(entity,where):
    """"""
    for exp in where:
        key=exp[0]
        value=exp[2]
        op=exp[1]

        en=entity[key]

        if op=='>'  and not en>value:
            return False
        elif op=='<' and not en<value:
            return False
        elif op=='=' and not  en==value:
            return False
        elif op=='<=' and not  en<=value:
            return False
        elif op=='>=' and not  en>=value:
            return False
        elif op=='!=' and not  en!=value:
            return False
    return True
    

def nameToIds(name,where):
    """"""
    ids=[]
    name=name.upper()
    if cur.execute('select id from '+md5+' where `name`=%s',(name)):
        allIds={i[0] for i in cur.fetchall()}
    else:
        allIds={}
    if where:
        for i in allIds:
            entity=getEntity(i)
            if validateExp(entity,where):
                ids.append(i)
    else:
        ids+=allIds
    return ids

def getParam(id):
    """"""
    if cur.execute('select param from '+md5+' where `id`=%s',str(id)):
        param=cur.fetchone()[0]
    return param

def getLines():
    """"""
    if not bitmap.count_bits():
        return []
    id=0
    ids=[]
    for bit in bitmap:
        if bit:
            ids.append(str(id)) 
        id+=1

    if cur.execute('select id,name,param from '+md5+' where `id` in (%s)'%(','.join(ids))):
        lines=cur.fetchall()
    return lines

def getEntity(id):
    """"""
    return db[md5].find_one({'id':id})

def getSubModel(srl,hash):
    """"""
    global md5,conn,cur,monConn,db
    conn,cur=getMysqlConn()
    monConn,db=getMongoConn()
    md5=hash
    visitEntities(parseSRL(srl))
    fileContent= generateModelFile(subids)
    cur.close()
    conn.close()
    monConn.close()
    return fileContent


if __name__ == '__main__':
    import time
    #parseSRL('rules/geo2.srl')
    #getSubModel('rules/geo2.srl','335af8fe4295cad94d270f29aff664d0')
    conn,cur=getMysqlConn()
    monConn,db=getMongoConn()
    #md5='335af8fe4295cad94d270f29aff664d0'
    md5='5de172dbe0db7fa9f590ab51fdcd28ad'
    #md5='193ab02b353e9d3a59d719c87ffbdc52'
    beg=time.time()
    visitEntities(parseSRL('rules/geo2.srl'))
    end=time.time()
    print end-beg
    print bitmap.count_bits()
    print bitmap.length()
    #fileContent= generateModelFile()
    cur.close()
    conn.close()
    monConn.close()
    #with open("output.ifc",'w') as fp:
        #fp.write(fileContent)

