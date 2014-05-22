#!/usr/bin/python
#coding=utf-8
#Filename:SPFHeader.py
from utils import parseList,getLine,fromSPF
from serializable import Serializable
import log

class FileDescription(Serializable):
    """"""
    def __init__(self):
        super(FileDescription,self).__init__()
        self.description=[]
        self.implementationLevel=''

    def toDict(self):
        """"""
        return [''.join(self.description),self.implementationLevel]

class FileName(Serializable):
    """"""
    def __init__(self):
        super(FileName,self).__init__()
        self.name=''
        self.author=[]
        self.organization=[]
        self.preprocessorVersion=''
        self.originatingSystem=''
        self.authorization=''

    def toDict(self):
        """"""
        return [self.name,''.join(self.author),''.join(self.organization),self.preprocessorVersion,self.originatingSystem,self.authorization]

class FileSchema(Serializable):
    """"""
    def __init__(self):
        super(FileSchema,self).__init__()
        self.schemaIdentifiers=[]

    def toDict(self):
        """"""
        return [''.join(self.schemaIdentifiers)]

class SPFHeader(Serializable):
    """ a parser and storage of the ifc header
    """
    def __init__(self):
        super(SPFHeader,self).__init__()
        self.fileDescription=FileDescription()
        self.fileName=FileName()
        self.fileSchema=FileSchema()
        self.otherFields=''

    def parse(self,fp):
        """parse the header of ifc file
        """

        s=getLine(fp)
        if not s or s !="ISO-10303-21":
            log.error("SPFHeader : Bad file type, should be ISO-10303-21.")
            return False

        s=getLine(fp)
        if not s or  s!="HEADER":
            log.error("SPFHeader : Can't find the HEADER section.")
            return False
        
        # FILE_DESCRIPTION arguments
        #give a (..) and get a vector of arguments
        #FILE_DESCRIPTION (('ArchiCAD 7.00 Release 2 generated IFC file.', 
        #'Build Number of the Ifc 2x interface: 00054 (01-10-2002)'), '2;1');
        s=getLine(fp)
        i=s.find('(') 
        if not s.startswith("FILE_DESCRIPTION"):
            log.error("SPFHeader : Can't find the FILE_DESCRIPTION argument.")
            return False
        currentParam=parseList(s[i+1:-1])
        if not currentParam  or len(currentParam)!=2:
            log.error("SPFHeader : Bad number of arguments for FILE_DESCRIPTION, should be 2")
            return False

        vec=parseList(currentParam[0][1:len(currentParam[0])-1])
        if not vec:
            log.error("SPFHeader : Syntax Error in arg 1 of FILE_DESCRIPTION");
            return False
    
        for arg in vec:
            self.fileDescription.description.append(fromSPF(arg))         
        self.fileDescription.implementationLevel=fromSPF(currentParam[1])

        s=getLine(fp)
        i=s.find('(')       
        if not s.startswith("FILE_NAME"):
            log.error("SPFHeader : Can't find the FILE_DESCRIPTION argument.")
            return False
        currentParam=parseList(s[i+1:-1])
        if not currentParam:
            log.error(" SPFHeader : Bad number of arguments for FILE_DESCRIPTION, should be 7 ")
            return False

        self.fileName.name=fromSPF(currentParam[0])
        self.fileName.timeStamp=currentParam[1]
        
        vec=parseList(currentParam[2][1:-1])
        if not vec:
            log.error("SPFHeader : Syntax Error in arg 3 of FILE_NAME")
            return False
        for arg in vec:
            self.fileName.author.append(fromSPF(arg))

        vec=parseList(currentParam[3][1:-1])
        if not vec:
            log.error("SPFHeader : Syntax Error in arg 4 of FILE_NAME")
            return False
                
        for arg in vec:
            self.fileName.organization.append(fromSPF(arg))

        self.fileName.preprocessorVersion=fromSPF(currentParam[4])
        self.fileName.originatingSystem =fromSPF(currentParam[5])
        self.fileName.authorization =fromSPF(currentParam[6])

        s=getLine(fp)
        i=s.find('(')
        if not s.startswith("FILE_SCHEMA"):
            log.error("SPFHeader : Can't find the FILE_SCHEMA argument.")
            return False

        currentParam=parseList(s[i+1:-1])
        vec=parseList(currentParam[0][1:-1])
        for arg in vec:
            self.fileSchema.schemaIdentifiers.append(fromSPF(arg))

        self.otherFields=''
        found=False
        for i in range(0,5):
            s=getLine(fp)
            if not s:
                return False
            if s=="ENDSEC":
                found=True
                break
            self.otherFields+=s
        if not found:
            log.error("SPFHeader : Can't find ENDSEC")
            return False
        return True
        
if __name__ == '__main__':
    log.InitLog()
    header=SPFHeader()
    fp=file("files/room.ifc",'r')
    header.parse(fp)
    print header.fileDescription.Serialize()
    print header.fileName.Serialize()
    print header.fileSchema.Serialize()
