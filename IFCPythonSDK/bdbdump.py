#!/usr/bin/python
#coding=utf-8
#Filename:bdbdump.py
import bsddb3 as bsddb
home = "db_home"
#md5='193ab02b353e9d3a59d719c87ffbdc52'
#md5='335af8fe4295cad94d270f29aff664d0'
md5='ed9d6a7690a5e3e77d713f761f9aecad'


if __name__ == '__main__':
    dbenv = bsddb.db.DBEnv()
    dbenv.open(home, bsddb.db.DB_CREATE | bsddb.db.DB_INIT_MPOOL)
    d = bsddb.db.DB(dbenv)
    # btree是 bsddb.db.DB_BTREE， hash是bsddb.db.DB_HASH
    # queu 是 bsddb.db.DB_QUEUE,  recno 是bsddb.db.DB_RECNO
    d.open(md5, bsddb.db.DB_BTREE, bsddb.db.DB_CREATE, 0666)
    """"""
    for key in d.keys():
        print key.center(70,'*')
        print d.get(key).decode('utf-8')
        
    # 插入一条数据，注意queue和recno的key不能是字符串的，应该是数字
    # d.put('test1', 'zhaowei')    
    d.close()
    dbenv.close()


