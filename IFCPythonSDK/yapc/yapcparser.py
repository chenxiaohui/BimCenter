#!/usr/bin/python
#coding=utf-8
#Filename:parser.py

import log
from dataset import DataSet
from schemaparser import parseSchema
from preprocessor import preprocess
from generator import Generator

class Parser(object):
    """"""
    def __init__(self):
        super(Parser,self).__init__()
        self.dataset=DataSet()
        
    def parse(self,fp):
        """"""
        if not fp:
            log.error("File cannot be opened.");
            return
        parseSchema(self.dataset,fp)
        #self.parseHeader(fp)
    
    #def parseHeader(self,fp):
        #""""""
        #header=''       
        #token=geti(fp)
        #if token=='(':#has copyright
            #token=geti(fp)
            #if token=='*':#copyright begins
                #while token!=')':
                    #token=geti(fp)
                    #if token=='*':
                        #token=geti(fp)
                        #if token==')':#copyright ends
                            #self.dataset.header=header
                    #header+=token+" "
        #else:
            #back(fp)

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
    with open('myschema.json','w') as fp:
        toJson(dataset.types,fp)
        toJson(dataset.entities,fp)
        toJson(dataset.rules,fp)
        toJson(dataset.functions,fp)

    generater=Generator(dataset)
    generater.generateCommonFiles()
    generater.generateTypes()
    generater.generateEntities()
    generater.generateIndexes()
