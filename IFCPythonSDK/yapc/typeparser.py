#/usr/bin/python
#coding=utf-8
#Filename:typeparser.py

import common
import log
from utils import geti,back
from commonparser import parseWhere ,parseBaseType
from type import Type
    
def parseType(fp,dataset):
    """
        type_decl = TYPE type_id '=' underlying_type ';' [where_clause] END_TYPE ';' .
        type_id = simple_id .
    """
    tp=Type()

    #type name 
    name=geti(fp)   

    token=geti(fp)
    if token!='=':
        log.error('Type has no equal symbol, line %d'%common.counter)
        return
    
    # underlying type
    tp.content=parseUnderlyingType(fp)
    
    token=geti(fp)#skip ;   
    if token!=';':
        log.error('Type content does not end with ;, line %d'%common.counter)
        return

    # parse where clause
    tp.where=parseWhere(fp)       

    #parse END_TYPE
    token=geti(fp)
    if token!='END_TYPE':
        log.error('Type Defination has no END_TYPE, line %d'%common.counter)
        return
    token=geti(fp)#skip ;   
    if token!=';':
        log.error('Type Defination does not end with ;, line %d'%common.counter)
        return
    
    dataset.types[name]=tp


def parseUnderlyingType(fp):
    """
        underlying_type = enumeration_type | select_type | aggregation_types | simple_types | type_ref .
    """
    token=geti(fp)
    back(fp)
    if token=='SELECT':
        return parseSelectType(fp)
    elif token=='ENUMERATION':
        return parseEnumType(fp)
    else:
        return parseBaseType(fp)

def parseEnumType(fp):
    """
        enumeration_type = ENUMERATION OF '(' enumeration_id {','enumeration_id} ')' .
        enumeration_id = simple_id .
    """
    token=geti(fp)
    enum={'TYPE':'ENUMERATION'}
    #OF
    token=geti(fp)
    if token!='OF':
        log.error('ENUMERATION Defination has no OF, line %d'%common.counter)
        return
    #(
    token=geti(fp) 
    if token!='(':
        log.error('ENUMERATION Defination has no (, line %d'%common.counter)
        return

    #ids
    values=[]
    token=geti(fp)
    while token!=')':
        values.append(token)
        token=geti(fp)
        if token==',':
            token=geti(fp)
    
    enum['VALUES']=values
    return enum

def parseSelectType(fp):
    """
        select_type = SELECT '(' named_types { ',' named_types } ')' .
        named_types = entity_ref | type_ref .
    """
    token=geti(fp)
    select={'TYPE':'SELECT'}
    #(
    token=geti(fp) 
    if token!='(':
        log.error('SELECT Defination has no (, line %d'%common.counter)
        return

    #values
    values=[]
    token=geti(fp)
    while token!=')':
        values.append(token)
        token=geti(fp)
        if token==',':
            token=geti(fp)
    
    select['VALUES']=values
    return select


#if __name__ == '__main__':
    #try:
        #import cStringIO as StringIO
    #except Exception :
        #import StringIO

    #fp = StringIO.StringIO("""
     #IfcCompoundPlaneAngleMeasure = LIST [3:4] OF INTEGER;
     #WHERE
        #WR1 : { -360 <= SELF[1] < 360 };
        #WR2 : { -60 <= SELF[2] < 60 };
        #WR3 : { -60 <= SELF[3] < 60 };
        #WR4 : ((SELF[1] >= 0) AND (SELF[2] >= 0) AND (SELF[3] >= 0)) OR ((SELF[1] <= 0) AND (SELF[2] <= 0) AND (SELF[3] <= 0));
    #END_TYPE;
                          #""")
    #from dataset import DataSet
    #dataset=DataSet()
    #parseType(fp,dataset)
    #for key,item in dataset.types.items():
        #print key
        #print item.Serialize()
    

