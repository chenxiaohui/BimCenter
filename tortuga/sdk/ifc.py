#!/usr/bin/python
#coding=utf-8
#Filename:upload.py

import sys
import hashlib
from django.core.files.storage import FileSystemStorage  
from django.conf import settings  
sys.path.append("..")
sys.path.append("../IFCPythonSDK/")
from IFCPythonSDK import *

def CalcHash(fieldfile):
    md5obj = hashlib.md5()
    md5obj.update(fieldfile.read())
    hash = md5obj.hexdigest()
    return hash

def parseIFC(filename,hash,mid=None,increment=False):
    """"""
    log.InitLog()
    
    reader=SPFReader()
    with file(filename,"r") as fp:
    #with file("files/room.ifc","r") as fp:
        reader.read(fp)
    expDataSet=reader.expDataSet
    expDataSet.instantiateAll()

    model=SubModel()
    with open(filename,'r') as fp:
        model.read(fp)

    toMySQL(model,expDataSet,hash,int(mid),increment)

def deleteModelVersion(model_id,version):
    """"""
    log.InitLog()
    print dir()
    deleteVersion(model_id,version)

def toSubModel(srl,hash):
    """"""
    return getSubModel(srl,hash)
#class IFCStorage(FileSystemStorage):  
      
    #def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):  
        #super(IFCStorage, self).__init__(location, base_url)  
  
    #def _save(self, name, content):  
        #import os.path,hashlib
        #path=os.path.dirname(name)
        #md5obj = hashlib.md5()
        #md5obj.update(content.read())
        #hash = md5obj.hexdigest()

        #name=os.path.join(path,hash+'.ifc')
        #return super(IFCStorage, self)._save(name, content)  
#from django.http import HttpResponse
#from django.shortcuts import render_to_response
#def test(request):
    #""""""
    #if request.method=='GET':
        #return render_to_response('upload.html')
    #else:
        #return HttpResponse(request.method)
