#!/usr/bin/python
#coding=utf-8
#Filename:tojson.py

def toJson(items,md5,append=False):
    """"""
    flag='a' if append  else 'w'
    with open('files/'+md5,flag) as fp:
        for key,value in items.items():
            fp.write(str(key).center(70,'*')+'\n')
            fp.write(value.Serialize()+'\n')
