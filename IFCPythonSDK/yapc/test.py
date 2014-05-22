#!/usr/bin/python
#coding=utf-8
#Filename:test.py
import json
import log
class Entity(object):
    """"""
    def __init__(self):
        super(Entity,self).__init__()
        self.name='cxh'
        self.content={'age':12,'locate':'china'}

class ComplexEntity(Entity):
    def __init__(self):
        super(ComplexEntity,self).__init__()
        self.name='xxx'

    def Serialize(self):
        """"""
        print json.dumps(self.__dict__)
#items={
        #"Description": {
            #"OPTIONAL": 1, 
            #"TYPE": "IfcText", 
            #"ID": 2
        #}, 
        #"Addresses": {
            #"BASETYPE": {
                #"TYPE": "IfcAddress"
            #}, 
            #"UBOUND": "?", 
            #"OPTIONAL": 1, 
            #"REF": 1, 
            #"LBOUND": 1, 
            #"TYPE": "LIST", 
            #"ID": 4
        #}, 
        #"Id": {
            #"OPTIONAL": 1, 
            #"TYPE": "IfcIdentifier", 
            #"ID": 0
        #}, 
        #"Roles": {
            #"BASETYPE": {
                #"TYPE": "IfcActorRole"
            #}, 
            #"UBOUND": "?", 
            #"OPTIONAL": 1, 
            #"LBOUND": 1, 
            #"TYPE": "LIST", 
            #"ID": 3
        #}, 
        #"Name": {
            #"TYPE": "IfcLabel", 
            #"ID": 1
        #}
#}
#results=[]
#for key,value in items.items():
    #value['KEY']=key
    #results.append(value)
#print sorted(results,key=lambda x:x['ID'])
#items=[{'id':1,'name':'cxh'},{'id':3,'name':'mengli'},{'id':2,'name':'xiaoyuan'}]
#print sorted(items,key=lambda x:x['name'])
#fp=file('test.in','rb')
#print id(fp)

#try:
    #import cStringIO as StringIO
#except Exception :
    #import StringIO

#s = StringIO.StringIO("JGood is a handsome boy")
#print id(s)

#class IfcActionTypeEnum():
    #""""""
    #PERMANENT_G=0
    #VARIABLE_Q=1
    #EXTRAORDINARY_A=2
    #USERDEFINED=3
    #NOTDEFINED=4
    
#print dir(IfcActionTypeEnum)
#import re
#args={"test":"google",'name':'chenxiaohui'}
#print args.get('te',args.get('name'))
#args={"test":"google",'name':'chenxiaohui'}
#code="sss {test|upper} ss {name}"
#p=re.compile(r"\{.+?}")
#pos=p.search(code)
#while pos:
    #ops=pos.group()[1:-1].split('|')
    #if len(ops)<1:
        #log.err("Argument in template %s is empty."%'todo')
        #break
    #key=ops[0]
    #if not key in args:
        #log.err("Argument %s in template %s not supplied."%(key,'todo'))
        #break
    #arg=args[key]
    ##ops
    #del(ops[0])
    #for op in ops:
        #if op.lower()=='title':  
            #arg=arg.title()
        #elif op.lower()=='upper':  
            #arg=arg.upper()
        #elif op.lower()=='lower':  
            #arg=arg.lower()
    ##replace
    #code=code[:pos.start()]+arg+code[pos.end():]
    #pos=p.search(code)

#print code
a=None
if a==None:
    print 'yes'
else:
    print 'no'

