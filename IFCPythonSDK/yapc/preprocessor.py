#!/usr/bin/python
#coding=utf-8
#Filename:preprocessor.py
import log
import copy
def processInverse(dataset):
    """register inverse to dataset.entities
    """
    entities=dataset.entities
    for entity in entities.values():
        if entity.inverse:#has inverse
            for inverse in entity.inverse.values():
                #register attribute has inverse
                target=inverse.get('BASETYPE',inverse['TYPE'])
                if target in entities:
                    for attr in entities[target].attribute:
                        if attr['KEY']==inverse['FOR']:
                            attr['REF']=1
                            break

BASETYPE=['NUMBER','INTEGER','REAL','LOGICAL','BOOLEAN','BINARY','STRING']
AGGREGATIONTYPE=['BAG','LIST','ARRAY','SET']

def isSimpleType(ty):
    """"""
    return (ty in BASETYPE or ty=='ENUMERATION' or ty=='SELECT')

def getRealType(ty,types):
    """"""
    if isSimpleType(ty):
        return {'TYPE':ty}
    else:#ref type
        if not ty in types:
            log.error("RefType %s not defined."%ty)
        else:
            tyobj=copy.deepcopy(types[ty].content)
            nty=tyobj['TYPE']
            if nty in AGGREGATIONTYPE:
                tyobj['BASETYPE']=getRealType(tyobj['BASETYPE']['TYPE'],types)
                return tyobj
            if nty=='ENUMERATION' or nty=='SELECT':
                return {'TYPE':ty}
            else:
                return getRealType(nty,types)

def processTypeDef(dataset):
    """find the real type of all attributes
    """
    types=dataset.types
    for key,tyobj in types.items():
        ty=tyobj.content['TYPE']
        if isSimpleType(ty):
            continue
        elif ty in AGGREGATIONTYPE:
            realtype=tyobj.content['BASETYPE']['TYPE']
            tyobj.content['BASETYPE']=getRealType(realtype,types)
        else:#ref type
            if not ty in types:
                log.error("RefType %s not defined."%ty)
                return None
            else:
                tyobj.content=getRealType(ty,types)

def preprocess(dataset):
    """"""
    processInverse(dataset)
    processTypeDef(dataset)
