#!/usr/bin/python
#coding=utf-8
#Filename:ruleparser.py


import common
import log
from utils import geti
from commonparser import parseWhere,parseLocal,parseCode
from rule import Rule

    

def parseRule(fp,dataset):
    """"""
    rule=Rule()      
    
    #rule name 
    name=geti(fp)   

    #for
    token=geti(fp)
    if token!='FOR':
        log.error('Rule has no FOR symbol, line %d'%common.counter)
        return

    #(
    token=geti(fp)
    if token!='(':
        log.error('Rule FOR has no ( symbol, line %d'%common.counter)
        return

    #for..
    token=geti(fp)
    rule.target=token

    #)
    token=geti(fp)
    if token!=')':
        log.error('Rule FOR brackets not match , line %d'%common.counter)
        return
    
    #;
    token=geti(fp)
    if token!=';':
        log.error('Rule FOR not end with ; , line %d'%common.counter)
        return

    #local
    parseLocal(fp,rule)

    #code
    parseCode(fp,rule)

    # where clause
    rule.where=parseWhere(fp)       

    #parse END_RULE
    token=geti(fp)
    if token!='END_RULE':
        log.error('RULE Defination has no END_RULE, line %d'%common.counter)
        return
    token=geti(fp)#skip ;   
    if token!=';':
        log.error('RULE Defination does not end with ;, line %d'%common.counter)
        return

    dataset.rules[name]=rule
