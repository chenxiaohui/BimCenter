#!/usr/bin/python
#coding=utf-8
#Filename:schemaparser.py
import log
import common
from utils import geti
from entityparser import parseEntity
from typeparser import parseType
from ruleparser import parseRule
from functionparser import parseFunction
from procedureparser import parseProcedure

def parseSchema(dataset,fp):
    """ 
        schema_block = SCHEMA schema_id ';' schema_body END_SCHEMA ';' .
        schema_id = simple_id .
        schema_body = { interface_specification } [constant_dec1] {declaration | rule_block } .
        declaration = entity_block | function_block | procedure_block | type_dec1 .
    """
    token=geti(fp)
    if token!='SCHEMA':
        log.error("File Content not starts with Schema in line%d"%common.counter);
        return

    token=geti(fp)
    while token!=';':
        dataset.schemaName+=token
        token=geti(fp)

    token=geti(fp)
    while token!='END_SCHEMA':
        if token=='ENTITY':
            parseEntity(fp,dataset)
        elif token=='TYPE':
            parseType(fp,dataset)
        elif token=='FUNCTION':
            parseFunction(fp,dataset)
        elif token=='RULE':
            parseRule(fp,dataset)
        elif token=='PROCEDURE':
            parseProcedure(fp,dataset)
        token=geti(fp)

    token=geti(fp)
    if token!=';':
        log.error("File Content not ends with ; in line%d"%common.counter);
        return

def parseInterfaceSpec(fp):
    """
        interface_specification = reference_clause | use_clause .
    """
    pass
    
def parseRefrenceClause(fp):
    """"""

def parseUseClause(fp):
    """"""

def parseConstantDecl(fp):
    """ 
        constant_dec1 = CONSTANT { constant_body } END_CONSTANT ';' .
        constant_body = constant_id ':' base_type ':=' expression ';' .
        constant_id = simpled_id .
    """
    pass

    
