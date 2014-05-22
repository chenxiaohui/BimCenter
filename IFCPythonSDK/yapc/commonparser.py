#!/usr/bin/python
#coding=utf-8
#Filename:commonparser.py
import log
import common
from utils import geti,back

def parseWhere(fp):
    """
        where_clause = WHERE labelled_expression ';' { labelled_expression ':' } .
        labelled_expression = [ label ':' ] expression .
        label = simpled_id .
    """
    where={}
    token=geti(fp)
    if token!='WHERE':
        back(fp)
        return where

    token=geti(fp)#a key
    while not token.startswith("END"):
        key=token
        token=geti(fp)#:
        if token!=":":
            log.error('Where clause has no colon , line %d'%common.counter)
            return
        clause=''
        token=geti(fp)
        while token!=';':
            clause+=token+' '
            token=geti(fp)

        token=geti(fp)
        where[key]=clause.strip()
    
    back(fp)
    return where

def parseLocal(fp,obj):
    """
      LOCAL
        IsDifferent  : LOGICAL := FALSE;
        Result : IfcVector;
        Res, Vec1, Vec2 : IfcDirection;
      END_LOCAL;
    """
    #parse Local
    token=geti(fp)
    if token!='LOCAL':
        back(fp)
        return
    token=geti(fp)#var name
    while token!='END_LOCAL':
        args=[token]
        token=geti(fp)#test , or :
        if token==',':
            while token!=':':
                token=geti(fp)
                args.append(token)
                token=geti(fp)#, or :

        if token==':' :
            value=''
            token=geti(fp)
            while token!=';':
                value+=token+' '
                token=geti(fp)
                
        #add locals
        for var in args:
            obj.local[var]=value.strip()

        #next element
        token=geti(fp)

    token=geti(fp)#skip ;   
    if token!=';':
        log.error('Local does not end with ;, line %d'%common.counter)
        return

def parseCode(fp,obj):
    """"""
    #parse code
    token=geti(fp)
    if token=='WHERE' or token.startswith('END'):
        back(fp)
        return

    #code
    code=''
    while token!='WHERE' and not token.startswith('END'):
        code+=token+' '
        token=geti(fp)
    obj.code=code.strip()
    back(fp)

        
def parseBaseType(fp):
    """ 
        base_type = aggregation_types | simple_types | named_types
    """
    token=geti(fp)
    back(fp)
    if token in ['NUMBER','INTEGER','LOGICAL','BOOLEAN','REAL','STRING','BINARY']:#simpletype
        return parseSimpleType(fp)
    elif token in['ARRAY','BAG','LIST','SET']:
        return parseAggregationType(fp)
    else:
        return parseNamedType(fp)

def parseAggregationType(fp):
    """
        aggregation_types = array_type | bag_type | list_type | set_type .
    """
    #type name
    name=geti(fp)
    ty={'TYPE':name}  

    token=geti(fp)
    if token!='[':
        log.error('%s bound has no [ , line %d'%(name,common.counter))
        return

    token=geti(fp)
    try:
        ty['LBOUND']=int(token)
    except Exception :
        log.error('%s lower bound is not integer , line %d'%( name,common.counter ))
        return

    token=geti(fp)
    if token!=':':
        log.error('%s bound has no : , line %d'%( name,common.counter ))
        return
    
    token=geti(fp)
    if token=='?':
        ty['UBOUND']='?'
    else:
        try:
            ty['UBOUND']=int(token)
        except Exception :
            log.error('%s upper bound is not integer or ? , line %d'%(name, common.counter ))
            return

    token=geti(fp)
    if token!=']':
        log.error('%s bound has no ] , line %d'%( name,common.counter ))
        return
    
    token=geti(fp)
    if token!='OF':
        log.error('%s has no OF , line %d'%( name,common.counter ))
        return
    token=geti(fp)   
    if token=='OPTIONAL':
        ty['OPTIONAL']=1
        token=geti(fp)
    if token=='UNIQUE':
        ty['UNIQUE']=1
        token=geti(fp)
    back(fp)
    ty['BASETYPE']=parseBaseType(fp)
    return ty 

def parseSimpleType(fp):
    """
        simple_types = binary_type | boolean_type | integer_type | logical_type | number_type | real_type | string_type .
    """
    ty={}
    token=geti(fp)
    if token in ['NUMBER','INTEGER','LOGICAL','BOOLEAN']:#simpletype
        ty['TYPE']=token
    elif token=='REAL':
        ty['TYPE']=token
        token=geti(fp)
        try:
            ty['PRECISION']=int(token)
        except Exception:
            back(fp)
    elif token=='STRING' or token=='BINARY':
        ty['TYPE']=token
        token=geti(fp)
        if token=='(':
            token=geti(fp)
            try:
                ty['WIDTH']=int(token)
            except Exception:
                log.error(token+' WIDTH is not integer , line %d'%common.counter)
                return
            token=geti(fp)
            if token!=')':
                log.error(token+' declaration brackets not match, line %d'%common.counter)
                return
            token=geti(fp)
            if token=='FIXED':
                ty['FIXED']=1              
            else:
                back(fp)
        else:
            back(fp)
    
    return ty
    
def parseNamedType(fp):
    """
        named_types = entity_ref | type_ref .
    """
    token=geti(fp)
    ty={'TYPE':token}
    return ty

#if __name__ == '__main__':
    #try:
        #import cStringIO as StringIO
    #except Exception :
        #import StringIO

    #s = StringIO.StringIO(" is a handsome boy")
    #print id(s)
