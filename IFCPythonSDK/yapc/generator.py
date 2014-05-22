#!/usr/bin/python
#coding=utf-8
#Filename:generator.py
import log
from utils import render,getList

BASETYPE={'NUMBER':'None','INTEGER':'None','REAL':'None','LOGICAL':'None','BOOLEAN':'None','BINARY':'None','STRING':'None'}
#BASETYPE={'NUMBER':'0','INTEGER':'0','REAL':'0.0','LOGICAL':'True','BOOLEAN':'True','BINARY':'[]','STRING':'\'\''}
AGGREGATIONTYPE=['BAG','LIST','ARRAY','SET']
FUNCFROM={'NUMBER':'spfToInteger','INTEGER':'spfToInteger','REAL':'spfToInteger',
      'LOGICAL':'spfToLogical','BOOLEAN':'spfToLogical',
      'BINARY':'spfToBinary','STRING':'fromSPF',
      'BAG':'getIdListParam','LIST':'getIdListParam',
      'ARRAY':'getIdListParam','SET':'getIdListParam',
      'ENUMERATION':'spfToTypeRef','SELECT':'spfToTypeRef',
      'ENTITYREF':'spfToId'
     }
FUNCTO={'NUMBER':'integerToSPF','INTEGER':'integerToSPF','REAL':'integerToSPF',
      'LOGICAL':'logicalToSPF','BOOLEAN':'logicalToSPF',
      'BINARY':'binaryToSPF','STRING':'strToSPF',
      'BAG':'listParamToSPF','LIST':'listParamToSPF',
      'ARRAY':'listParamToSPF','SET':'listParamToSPF',
      'ENUMERATION':'typerefToSPF','SELECT':'typerefToSPF',
      'ENTITYREF':'idToSPF'
     }
modules=[]

def getSuper(value):
    """"""
    return value.supertype.upper() if value.supertype else 'BaseObject'

def getImport(value):
    """"""
    if value=='BaseObject':
        return 'from baseobject import BaseObject'
    return 'from %s import %s\n'%(value.lower(),value.upper())
    
class Generator(object):
    """"""
    def __init__(self,dataset):
        super(Generator,self).__init__()
        self.dataset=dataset
        
    def generateSelect(self,key,content):
        """generate select type
        """
        render('select',
               {'name':key, 'selectlist':','.join(content['VALUES'])},
              key 
              )

    def generateEnum(self,key,content):
        """"""
        render('enum',
               {'name':key,'enumlist':getList(content['VALUES'],True)},
               'definedtypes',
               append=True,
              )     

    def generateCommonFiles(self):
        render('definedtypes',
               {},
               'definedtypes'
              )
        
    def generateTypes(self):
        for key,value in self.dataset.types.items():
            if value.content['TYPE']=='ENUMERATION':
                self.generateEnum(key,value.content)
            elif value.content['TYPE']=='SELECT':
                self.generateSelect(key,value.content)

    def generateEntities(self):
        for key,value in self.dataset.entities.items():
            self.generateEntity(key,value)
            modules.append(key)

    def generateIndexes(self):
        """"""
        code=''
        for entity in modules:
            code+=getImport(entity)
        render('initimport',
               {'imports':code},
               '__init__'
              )

    def generateEntity(self,key,value):
        """"""
        sup=getSuper(value);
        render('entity',
               {
                    'name':key,
                    'superclass':sup,
                    'superimport':getImport(sup),
                    'definations':self.getAttrList(value),
                    'load':self.getLoad(value,key),
                    'init':self.getInit(value),
                    'attrcount':len(value.attribute),
                    'tostring':self.getToString(value)
               },
                key 
              )    
    def getToString(self,value):
        """"""
        code=''
        for attr in value.attribute:
            func=self.getCmd(attr,FUNCTO,'self.'+attr['KEY'])
            code+=render('tostring',
                         {'func':func}
                        )
        return code

    def getAttrList(self,entity):
        code=''
        for attr in entity.attribute:
            code+=render('attrdefine',
                         {'key':attr['KEY'],
                          'value':self.getAttrInitValue(attr['TYPE']),
                          'type':attr['TYPE']}
                        )

        for key,value in entity.inverse.items():
            code+=render('inversedefine',
                         {'key':key,
                          'type':value['TYPE'],
                          'basetype':value.get('BASETYPE','Alone')}
                        )
        return code

    def getAttrInitValue(self,ty):
        """"""
        if ty in BASETYPE:#simple type
            return BASETYPE[ty]
        elif ty in AGGREGATIONTYPE:
            #return '[]'
            return 'None'
        else:#ref type or entities,find it's real type
            if not ty in self.dataset.types and not ty in self.dataset.entities:
                log.error("Type or Entity %s not defined."%ty)
                return 'None'
            #entity ref
            if ty in self.dataset.entities:
                return  'None'
            #type ref
            realtype=self.dataset.types[ty]
            ty=realtype.content['TYPE']
            if ty in BASETYPE:#simple type
                return BASETYPE[ty]
            #elif ty in AGGREGATIONTYPE:
                #return '[]'
            else:
                return 'None'

    def getLoad(self,entity,name):
        """"""
        idx=0
        code=''
        hasRef=False
        for attr in entity.attribute:
            if 'REF' in attr:#inverse
                func='getIdListParam' if attr['TYPE'] in AGGREGATIONTYPE else 'getIdParam'
                code+=render('load',
                             {'name':name,'attr':attr['KEY'],'idx':idx,'func':func},
                            )
                hasRef=1
            idx+=1
        if hasRef:
            code=render('basecount',
                         {'name':name},
                        )+code
        return code

    def getInit(self,entity):
        """"""
        code=''
        for attr in entity.attribute:
            func=self.getCmd(attr,FUNCFROM,'arg')
            code+=render('attrinit',
                         {'attr':attr['KEY'],
                          'func':func}
                        )
        
        for key,inverse in entity.inverse.items():
            code+=render('inverseinit',
                         {'ref':inverse.get('BASETYPE',inverse['TYPE']),
                          'attr':inverse['FOR'],
                          'key':key}
                        )
        return code

    def getTypeFunc(self,ty,FUNC):
        """ input:  type 
            return: the func
        """
        if ty in BASETYPE or ty in AGGREGATIONTYPE:
            return FUNC[ty]
        elif ty in self.dataset.types:
            basetype=self.dataset.types[ty].content
            bty=basetype['TYPE']
            if bty in BASETYPE or bty in ['ENUMERATION' ,'SELECT']:
                return FUNC[bty]
            else: #AGGREGATIONTYPE
                realtype=basetype['BASETYPE']
                return (FUNC[basetype['TYPE']],FUNC[realtype['TYPE']])
        elif ty in self.dataset.entities:
            return FUNC['ENTITYREF']
        else:
            log.error("Type or Entity %s not defined."%ty)
            return None
    

    def getCmd(self,attr,FUNC,arg):
        """ 
        """
        ty=attr['TYPE']
        if ty in AGGREGATIONTYPE:
            basetype=attr['BASETYPE']['TYPE']
            return '%s(%s,%s)'%(self.getTypeFunc(ty,FUNC),arg,self.getTypeFunc(basetype,FUNC))
        else:
            func=self.getTypeFunc(ty,FUNC)
            if isinstance(func,tuple):
                #print func
                return '%s(%s,%s)'%(func[0],arg,func[1])
            return '%s(%s)'%( func,arg )
