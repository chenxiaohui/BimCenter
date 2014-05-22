#!/usr/bin/python
#coding=utf-8
#Filename:toBsd.py

import bsddb3 as bsddb
import dict2xml
import tomongo
conn,db=tomongo.getConn()
home = "db_home"

def toBsd(items,md5):
    dbenv = bsddb.db.DBEnv()
    dbenv.open(home, bsddb.db.DB_CREATE | bsddb.db.DB_INIT_MPOOL)
    d = bsddb.db.DB(dbenv)
    # btree是 bsddb.db.DB_BTREE， hash是bsddb.db.DB_HASH
    # queu 是 bsddb.db.DB_QUEUE,  recno 是bsddb.db.DB_RECNO
    d.open(md5, bsddb.db.DB_BTREE, bsddb.db.DB_CREATE, 0666)
    """"""
    #d.put('zhao','long')
    head='<entity>\n'
    for key,value in items.items():
        content=dict2xml.dict2Xml(value.toDict(),head)+'</entity>'
        d.put(str(key),content)
    # 插入一条数据，注意queue和recno的key不能是字符串的，应该是数字
    # d.put('test1', 'zhaowei')    
    d.close()
    dbenv.close()



if __name__ == '__main__':
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET

    md5='193ab02b353e9d3a59d719c87ffbdc52'
    cur=db[md5]
    #md5='335af8fe4295cad94d270f29aff664d0'
    dbenv = bsddb.db.DBEnv()
    dbenv.open(home, bsddb.db.DB_CREATE | bsddb.db.DB_INIT_MPOOL)
    d = bsddb.db.DB(dbenv)
    # btree是 bsddb.db.DB_BTREE， hash是bsddb.db.DB_HASH
    # queu 是 bsddb.db.DB_QUEUE,  recno 是bsddb.db.DB_RECNO
    d.open(md5, bsddb.db.DB_BTREE, bsddb.db.DB_CREATE, 0666)

    from timeit import Timer
    def test1():
        """"""
        tree = ET.ElementTree(ET.fromstring(d.get('4412')))
        for item in  tree.findall('inverse/IsDefinedBy'):
            item.text

    def test2():
        """"""
        cur.find_one({'id':4412},{ 'inverse.IsDefinedBy':1,'_id':0 })

    t1=Timer("test1()","from __main__ import test1")
    t2=Timer("test2()","from __main__ import test2")
    print t1.timeit(1000)
    print t2.timeit(1000)
    d.close()
    dbenv.close()
