#!/usr/bin/python
#coding=utf-8
#Filename:BaseSPFReader.py
from utils import  getLine 
import log
import common

class BaseSPFReader(object):
    """"""
    def __init__(self):
        super(BaseSPFReader,self).__init__()

    def read(self,fp):
        """"""
        if not self.header.parse(fp):
            log.error("BaseSPFReader : Can't parse header section, line %d"%common.counter)
            return False

        #data section
        s=getLine(fp)
        if not s or s!='DATA':
            log.error("BaseSPFReader : Can't find DATA section, line %d"%common.counter)
            return False

        #id=ENTITYNAME(......)
        while True:
            beg=0
            #log.debug("Reading line %d"%common.counter)
            s=getLine(fp)
            if not s:
                log.error("BaseSPFReader : Unexpected End Of File, line %d"%common.counter)
                return False
            if s=="ENDSEC":
                break

            i=s.find('=')
            if i==-1 or s[0]!='#':
                log.error("BaseSPFReader : Syntax error on entity id, line %d"%common.counter)
                return False
            
            self.currentId=int(s[1:i])
            beg=i+1
            i=s.find('(',beg)
            if i==-1 or s[-1]!=')':
                log.error("BaseSPFReader : Syntax error on entity definition, line %d"%common.counter)
                return False
            entityName=s[beg:i]
            line=s[i+1:-1]
            
            currentObj=self.expDataSet.getSPFObject(self.currentId,entityName);
            currentObj.args.setParams(line)
            currentObj.load()
            #log.error("BaseSPFReader : Unexpected entity name : %s line" %(entityName,common.counter))

        s=getLine(fp)
        if not s or s!="END-ISO-10303-21":
            log.error("BaseSPFReader : Can't find END-ISO-10303-21 token, line %d"%common.counter)
            return False
        return True


