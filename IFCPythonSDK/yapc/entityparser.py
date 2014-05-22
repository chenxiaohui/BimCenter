#!/usr/bin/python
#coding=utf-8
#Filename:entityparser.py

import log
import common
from entity import Entity
from utils import geti,back
from commonparser import parseWhere,parseBaseType
end=['UNIQUE','INVERSE' ,'DERIVE','WHERE','END_ENTITY'];

def parseEntity(fp,dataset):
    """
        entity_block = entity_head entity_body END_ENTITY ';' .
        entity_head = ENTITY entity_id [subsuper] ';' .
        entity_id = simple_id .
        entity_body = {explicit_attr} [derive_clause] [inverse_clause] [unique_clause] [where_clause] .
        subsuper = [ supertype_declaration ] [ subtype_declaration ] .
    """
    en=Entity()

    #header
    name=geti(fp)   
    
    en.subtype=parseSuperType(fp)
    en.supertype=parseSubType(fp)

    #skip ;
    token=geti(fp)
    if token!=';':
        log.error("SubType not end with ; ,line%d"%common.counter)
        return 
    
    #content
    en.attribute=parseAttribute(fp)
    en.derive=parseDerive(fp)
    en.inverse=parseInverse(fp)
    en.unique=parseUnique(fp);
    en.where=parseWhere(fp)

    #parse END_ENTITY
    token=geti(fp)
    if token!='END_ENTITY':
        log.error('Entity Defination has no END_ENTITY, line %d'%common.counter)
        return
    token=geti(fp)#skip ;   
    if token!=';':
        log.error('Entity Defination does not end with ;, line %d'%common.counter)
        return

    dataset.entities[name]=en

def parseSuperType(fp):
    """
        supertype_declaration = ( ABSTRACT SUPERTYPE ) | ( [ ABSTRACT ] ) SUPERTYPE OF '(' supertype_expression ')' ) .
    """
    #super type
    token=geti(fp)
    if token=='SUPERTYPE':
        pass
    #abstract super type
    elif token=='ABSTRACT':
        token=geti(fp)
        if token=='SUPERTYPE':
            token=geti(fp)
            back(fp)
            if token!='OF':#root type
                return []
        else:
            log.error("Abstract has no SuperType symbol,line%d"%common.counter)
            return []
    else:#no supertype delcare
        back(fp)   
        return []
        
    token=geti(fp)   
    if token!='OF':
        log.error("SuperType has no OF symbol,line%d"%common.counter)
        return []

    token=geti(fp)
    if token!='(':
        log.error("SuperType OF has no ( symbol,line%d"%common.counter)
        return []
    
    st=parseSuperTypeExpression(fp)

    #the second )
    token=geti(fp)
    if token!=')':
        log.error("SuperType brackets not match ,line%d"%common.counter)
        return []

    return st

def parseSuperTypeExpression(fp):#super type expression
    """
        supertype_expression = supertype_factor { ( AND | ANDOR ) supertype_factor } .
    """
    st=parseSuperTypeFactor(fp)
    token=geti(fp)
    if token=='AND' or token=='ANDOR':
        sst=[st]
        while token=='AND' or token=='ANDOR':
            sst.append(parseSuperTypeFactor(fp))
            token=geti(fp)
        back(fp)
        return sst
    else:
        back(fp)
        return st

def parseSuperTypeFactor(fp):
    """
        supertype_factor = entity_ref | one_of | '(' supertype_expression ')' .
        one_of = ONEOF '(' supertype_expression { '.' supertype_expression } ')' .
    """
    token=geti(fp)
    if token=='(':#supertype expresssion
        st=parseSuperTypeExpression(fp)
        token=geti(fp)
        if token!=')':
            log.error("SuperType brackets not match ,line%d"%common.counter)
            return 
        return st
    elif token=='ONEOF':
        st=[]
        token=geti(fp)
        if token!='(':
            log.error("SuperType OF has no ( symbol,line%d"%common.counter)
            return 
        while token!=')':
            st.append(parseSuperTypeExpression(fp))
            token=geti(fp)#,

        return st
    else:#entity ref id
        return token

def parseSubType(fp):
    """
        subtype_declaration = SUBTYPE OF '(' entity_ref { '.' entity_ref } ')' .
    """
    
    #subtype
    token=geti(fp)
    if token!='SUBTYPE':
        back(fp)
        return
    
    token=geti(fp)   
    if token!='OF':
        log.error("SubType has no OF symbol,line%d"%common.counter)
        return 

    token=geti(fp)
    if token!='(':
        log.error("SubType OF has no ( symbol,line%d"%common.counter)
        return 

    #entity_ref
    token=geti(fp)
    st=token

    token=geti(fp)
    if token==',':
        st=[st]
        token=geti(fp)
        while token!=')':
            st.append(token)
            token=geti(fp)#,

    #the end )
    if token!=')':
        log.error("SubType brackets not match ,line%d"%common.counter)
        return 

    return st

def parseAttribute(fp):
    """
        explicit_attr = attribute_dec1 { ',' attribute_dec1 } ':' [OPTIONAL] base_type ';' .
    """
    attrs=[]
    #attr name
    token=geti(fp)
    if token in end:
        back(fp)
        return attrs 
    #tid=0
    while not token in end:
        #attr name
        attrname=[] 
        attrname.append(token)
        token=geti(fp)#, or :
        if token==',':
            token=geti(fp)
            while token!=':':
                attrname.append(token)
                token=geti(fp)

        token=geti(fp)
        if token=='OPTIONAL':
            optional=1
        else:
            optional=0
            back(fp)

        attrvalue=parseBaseType(fp)
        if optional:
            attrvalue['OPTIONAL']=1
       
        #add attribute
        for item in attrname:
            #attrvalue['ID']=tid
            attrvalue['KEY']=item
            attrs.append(attrvalue)
            #tid+=1
        
        token=geti(fp)
        if token!=';':
            log.error("Attribute has no ; ,line%d"%common.counter)
            return 
        
        #next token
        token=geti(fp)
    
    back(fp)#back one word
    return attrs
    
def parseDerive(fp):
    """
        derived_attr = attrivute_dec1 ':' base_type ':=' expression ';' .
    """
    #derive
    derives={}
    token=geti(fp)
    if token!='DERIVE':
        back(fp)
        return derives

    token=geti(fp)
    while not token in end:
        #name
        derivename=[] 
        derivename.append(token)
        token=geti(fp)#, or :
        if token==',':
            token=geti(fp)
            while token!=':':
                derivename.append(token)
                token=geti(fp)
        
        derivetype=parseBaseType(fp)
        
        token=geti(fp)
        if token!=':=':
            log.error("Derive has no := ,line%d"%common.counter)
            return 

        expression=''
        token=geti(fp)
        while token!=';':
            expression+=token+' '
            token=geti(fp)
        
        #add derive
        for item in derivename:
            derives[item]={'TYPE':derivetype,'VALUE':expression}

        #next token
        token=geti(fp)

    back(fp)#back one word
    return derives
    
#def parseAttributeDecl(fp):
    #"""
        #attribute_dec1 = attribute_id | referenced_attribute .
        #attribute_id = simple_id .
        #referenced_attribute = attribute_ref | qualified_attribute .
        #qualified_attribute = SELF group_qualifier attribute_qualifier .
        #group_qualifier = `\` entity_ref .
        #attribute_qualifier = '.' attribute_ref .
    #"""
    #token=geti(fp)
    #if token=='SELF':#qualified_attribute
        #attr=token
        #token=geti(fp)
        #if token!='\\':
            #log.error("Attribute SELF has no \ symbol,line%d"%common.counter)
            #return 
        #attr+='\\'
        #token=geti(fp)#entity ref
        #attr+=token
        #token=geti(fp)
        #if token!='.':
            #log.error("Attribute SELF has no . symbol,line%d"%common.counter)
            #return 
        #attr+='.'
        #token=geti(fp)
        #attr+=token
        #return attr
    #else:
        #return token

def parseInverse(fp):
    """
        inverse_attr = attribute_id =':' [ ( SET | BAG ) [ bound_spec ] OF ] entity_ref FOR attribute_ref ';' .
        attribute_id = simple_id .
        bound_spec = '[' bound_1 ':' bound_2 ']' .
        bound_1 = simple_expression .
        bound_2 = simple_expression .
    """
    #inverse
    inverses={}
    token=geti(fp)
    if token!='INVERSE':
        back(fp)
        return inverses

    token=geti(fp)
    while not token in end:
        #name
        name=token
        inverse={}
        #:
        token=geti(fp)
        if token!=':':
            log.error("Inverse has no colon ,line%d"%common.counter)
            return 

        token=geti(fp)
        if token=='SET' or token=='BAG':
            inverse['TYPE']=token   
            token=geti(fp)
            if token=='[':
                token=geti(fp)
                inverse['LBOUND']=int(token)
                token=geti(fp)
                if token!=':':
                    log.error("Inverse bound has no : ,line%d"%common.counter)
                    return 
                token=geti(fp)       
                inverse['UBOUND']=(token)
                token=geti(fp)
                if token!=']':
                    log.error("Inverse bound has no ] ,line%d"%common.counter)
                    return 
                token=geti(fp)
            if token=='OF':
                token=geti(fp)
                inverse['BASETYPE']=token
        else:
            inverse['TYPE']=token
        token=geti(fp)
        if token!='FOR':
            log.error("Inverse has no FOR ,line%d"%common.counter)
            return 
        token=geti(fp)
        inverse['FOR']=token
        
        token=geti(fp)
        if token!=';':
            log.error("Inverse has no ; ,line%d"%common.counter)
            return 

        #add inverse
        inverses[name]=inverse

        #next token
        token=geti(fp)

    back(fp)#back one word
    return inverses

def parseUnique(fp):
    """
        unique_clause = UNIQUE labelled_attrib_list ';' { labelled_attrib_list ';' } .
        labelled_attrib_list = [ label ':' ] referenced_attribute { ',' referenced_attribute } 
        label = simpled_id .
        referenced_attribute = attribute_ref | qualified_attribute .      
        qualified_attribute = SELF group_qualifier attribute_qualifier .
        group_qualifier = `\` entity_ref .
        attribute_qualifier = '.' attribute_ref .
    """
    #unique
    uniques={}
    token=geti(fp)
    if token!='UNIQUE':
        back(fp)
        return uniques

    #next elment
    token=geti(fp)
    while not token in end:
        #name
        name=token

        #:
        token=geti(fp)
        if token!=':':
            log.error("Unique has no colon ,line%d"%common.counter)
            return 

        #expression
        token=geti(fp)
        expression=''
        while token!=';':
            expression+=token+' '
            token=geti(fp)
        
        #add inverse
        uniques[name]=expression.strip()

        #next token
        token=geti(fp)
          
    back(fp)#back one word
    return uniques
       

#if __name__ == '__main__':
    #try:
        #import cStringIO as StringIO
    #except Exception :
        #import StringIO

    #fp = StringIO.StringIO("""
 #Ifc2DCompositeCurve
 #SUPERTYPE OF (ONEOF
	#(IfcOccupant))
 #SUBTYPE OF (IfcCompositeCurve);
    
	#RequestID : IfcIdentifier;

 #DERIVE
    #Z : SET [1:?] OF IfcDirection := NVL (IfcNormalise(Axis), IfcRepresentationItem() || IfcGeometricRepresentationItem () || IfcDirection([0.0,0.0,1.0]));
 #INVERSE
	#CoversSpaces : SET [0:1] OF IfcRelCoversSpaces FOR RelatedCoverings;
	#Covers : SET [0:1] OF IfcRelCoversBldgElements FOR RelatedCoverings;
 #UNIQUE
	#UR2 : ID;
 #WHERE
	#WR1 : SELF\IfcCompositeCurve.ClosedCurve;
	#WR2 : SELF\IfcCurve.Dim = 2;
#END_ENTITY;
                          #""")
    #from dataset import DataSet
    #dataset=DataSet()
    #parseEntity(fp,dataset)
    #for key,item in dataset.entities.items():
        #print key
        #print item.Serialize()
    
