#!/usr/bin/python
#coding=utf-8
#Filename:submodel.py
import log 
import re
import common
from spfheader import SPFHeader
from utils import getLine,render
pattern=re.compile(r'#(\d+)')

class SubModel(object):
    """"""
    def __init__(self):
        super(SubModel,self).__init__()
        self.lines={}
        self.header=SPFHeader()

    def read(self,fp):
        """ read lines to a dict:id->key(params) 
        """
        if not self.header.parse(fp):
            log.error("SubModel : Can't parse header section, line %d"%common.counter)
            return False

        #data section
        s=getLine(fp)
        if not s or s!='DATA':
            log.error("SubModel : Can't find DATA section, line %d"%common.counter)
            return False

        #id=ENTITYNAME(......)
        while True:
            beg=0
            s=getLine(fp)
            if not s:
                log.error("SubModel : Unexpected End Of File, line %d"%common.counter)
                return False
            if s=="ENDSEC":
                break

            i=s.find('=')
            if i==-1 or s[0]!='#':
                log.error("SubModel : Syntax error on entity id, line %d"%common.counter)
                return False
            
            entityId=int(s[1:i])
            beg=i+1
            i=s.find('(',beg)
            if i==-1 or s[-1]!=')':
                log.error("SubModel : Syntax error on entity definition, line %d"%common.counter)
                return False
            entityName=s[beg:i]
            params=s[i+1:-1]
            #print "#%s=%s(%s);"%(entityId,entityName,params)
            self.lines[entityId]=(entityName,params)

        s=getLine(fp)
        if not s or s!="END-ISO-10303-21":
            log.error("SubModel : Can't find END-ISO-10303-21 token, line %d"%common.counter)
            return False
        return True

    def getModelWithInverses(self,id):
        """ get sub model with explicit ref and inverses
        """
        pass

    def getModel(self,ids):
        """ get sub model with explicit ref
        """
        currentIds=ids if isinstance(ids,list) else [ids]
        idx=0
        while idx<len(currentIds):
            curId=currentIds[idx]
            if not curId in self.lines:
                log.error("SubModel : Can't find id %d, line %d"%(curId,common.counter))
                return None

            line=self.lines[curId]
            params=line[1]
            refs=pattern.findall(params)
            for ref in refs:
                if not int(ref) in currentIds:
                    currentIds.append(int(ref))
            idx+=1
        return sorted(currentIds)
        
    def getGeometryModel(self,id):
        """ get sub model only with geometry info
        """
        currentIds=[id]
        idx=0
        while idx<len(currentIds):
            curId=currentIds[idx]
            if not curId in self.lines:
                log.error("SubModel : Can't find id %d, line %d"%(curId,common.counter))
                return None

            line=self.lines[curId]
            params=line[1]
            refs=pattern.findall(params)
            for ref in refs:
                if not int(ref) in currentIds:
                    currentIds.append(int(ref))
            idx+=1
        return sorted(currentIds)

    def nameToIds(self,name):
        """"""
        ids=[]
        name=name.upper()
        for id,value in self.lines.items():
            if value[0]==name:
                ids.append(id)
        return ids
    
    def generateModelFile(self,ids,to):
        """"""
        code=''
        for i in ids:
            line=self.lines[i]
            code+='#%d=%s(%s);\n'%(i,line[0],line[1])

        render('temp.ifc',
               {'schema':','.join(self.header.fileSchema.schemaIdentifiers),'data':code},
              to)
    def getCategoryModel(self,categories):
        """"""
        ids=[]
        for category in categories:
            ids+=self.nameToIds(category)
        return self.getModel(ids)


if __name__ == '__main__':
    model=SubModel()
    with open("files/example.ifc",'r') as fp:
        res=model.read(fp)
        categories=['IFCWALLSTANDARDCASE','IFCSLAB','IFCDOOR','IFCCOLUMN','IFCBEAM','IFCWINDOW','IFCBUILDINGELEMENTPROXY']

        #model.generateModelFile(model.getModel([79,155,201,246]),'my.ifc')
        model.generateModelFile(model.getCategoryModel(categories),'my.ifc')
        import os
        os.system('viewer.exe files\\my.ifc')
