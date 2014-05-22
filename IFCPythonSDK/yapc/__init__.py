#!/usr/bin/python
#coding=utf-8
#Filename:__init__.py
import log
from preprocessor import preprocess
from generator import Generator
from yapcparser import Parser

def generateDot():
    """"""
    with open('output.dot','w') as fp:
        fp.write('digraph ifc2x3{\n')
        for key,value in dataset.entities.items():
            if value.supertype:
                fp.write("    %s->%s;\n"%(key,value.supertype))
        fp.write('}')

def toJson(items,fp):
    """"""
    #for key,item in items.items():
        #print key.center(80,'*')+'\n'
        #print item.Serialize()+'\n'

    for key,value in items.items():
        fp.write(key.center(70,'*')+'\n')
        fp.write(value.Serialize()+'\n')

    
if __name__ == '__main__':
    log.InitLog()       
    px=Parser()

    with open('IFC2X3_TC1.exp','rb') as fp:
    #with open('schema.exp','rb') as fp:
        px.parse(fp)

    dataset=px.dataset
    preprocess(dataset)
    with open('IFC2X3_TC1.json','w') as fp:
    #with open('schema.json','w') as fp:
        toJson(dataset.types,fp)
        toJson(dataset.entities,fp)
        toJson(dataset.rules,fp)
        toJson(dataset.functions,fp)

    generater=Generator(dataset)
    generater.generateCommonFiles()
    generater.generateTypes()
    generater.generateEntities()
    generater.generateIndexes()
