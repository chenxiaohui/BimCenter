#!/usr/bin/python
#coding=utf-8
#Filename:procedureparser.py

import common
import log
from utils import geti
from commonparser import parseWhere,parseLocal,parseCode
from procedure import Procedure

def parseProcedure(fp,dataset):
    """
    FUNCTION IfcVectorSum
	(Arg1, Arg2 : IfcVectorOrDirection)
	: IfcVector;
    """
    func=Procedure()      
    
    #Function name 
    name=geti(fp)   

    #args begin
    token=geti(fp)
    if token!='(':
        log.error('Function has no args, line %d'%common.counter)
        return

    #args
    token=geti(fp)
    while True:
        args=[token]
        token=geti(fp)
        if token==',':
            while token!=':':   
                token=geti(fp)
                args.append(token)
                token=geti(fp)
        if token==':':
            value=''
            token=geti(fp)              
            while token!=';' and token!=')':
                value+=token+' '
                token=geti(fp)              
            
        for arg in args:
            func.arg[arg]=value.strip()
        
        if token==')':
            break

        #next element
        token=geti(fp)
    
    #:
    token=geti(fp)
    if token!=':':
        log.error('Function ret has no :, line %d'%common.counter)
        return

    #ret
    ret=''
    token=geti(fp)
    while token!=';':
        ret+=token+' '
        token=geti(fp)

    func.ret=ret.strip()
    
    #local
    parseLocal(fp,func)

    #code
    parseCode(fp,func)

    # where clause
    func.where=parseWhere(fp)       

    #parse END_TYPE
    token=geti(fp)
    if token!='END_FUNCTION':
        log.error('FUNCTION Defination has no END_FUNCTION, line %d'%common.counter)
        return
    token=geti(fp)#skip ;   
    if token!=';':
        log.error('FUNCTION Defination does not end with ;, line %d'%common.counter)
        return

    dataset.functions[name]=func
