#!/usr/bin/python
#coding=
#Filename:toIFC.py
from utils import render
def toIFC(header,items,md5,append=False):
    """"""
    code=''
    for key,value in items.items():
        code+=(value.toCode()+'\n')


    return render('temp.ifc',
           {
                'description':','.join(header.fileDescription.description),
                'implementationLevel':header.fileDescription.implementationLevel,
                'name' :header.fileName.name,
                'author':','.join(header.fileName.author),
                'organization':','.join(header.fileName.organization),
                'preprocessorVersion':header.fileName.preprocessorVersion,
                'originatingSystem':header.fileName.originatingSystem,
                'authorization':header.fileName.authorization,
                'schemaIdentifiers':','.join(header.fileSchema.schemaIdentifiers),
                'data':code,
           }, md5,append)
