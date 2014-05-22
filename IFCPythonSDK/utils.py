#!/usr/bin/python
#coding=utf-8
#Filename:Utils.py
import common
import log
import os
import sys
import re
import hashlib

Apostrophe=39;  # '
Ampersand=38;  # &
Comma=44;   # ,
Colon=58;   # :
Semicolon=59;  # ;
Slash=47;   # / (the comment slash)
BackSlash=92;  # (the other slash, which indicates C line continuation)
Space=32;   # blank space
LeftParenthesis=40;
RightParenthesis=41;
Asterix=42;
DollarSign=36;
CrossHatch=35;  # #
Underscore=95;
Period=46;
EqualSign=61;
LessSign=60;  # <
GreaterSign=62;  # >
QuestionMark=63; #?
QuoteMark=34;  #"
PlusSign=43;
MinusSign=45;
LeftSquareBracket=91; # [
RightSquareBracket=93; # ]
LeftBracket=123;  # {
RightBracket=125;  # }
VerticalSlash=124;  # |
Hyphen=45;   # same as MinusSign
Newline = 10;
Return = 13;
#const to define value
ID_UNDEF =  sys.maxint
ID_UNSET = 0
UNKNOWN=-1


#variables in this file
bufferLength = 256000
i=-1
buff=''
templCache={}

def geti(fp):
    """"""
    global i,buff
    s=fp.read(1)
    if s=='' or i>=bufferLength-1:
        return None
    buff+=s
    i+=1
    return ord(s)

def getLine(fp):
    """ get a line from the  file
        example:
    """
    global i,buff
    i=-1
    buff=''
    beg=0
    res=''

    s=geti(fp)
    while s and s!=Semicolon: 
        if s>=0 and s<=32:#tab space enter
            if s==Newline:#end of line
                ++common.counter
            res+=buff[beg:i]
            beg=i+1
        elif s==Slash:#/  
            s=geti(fp)
            while s and s==Slash:
                s=geti(fp)
            if s==Asterix:#*
                res+=buff[beg:i-1]
                s=geti(fp)
                while s:
                    if s==Asterix:
                        s=geti(fp)
                        while s==Asterix:#remove duplicate *
                            s=geti(fp)
                        if s==Slash:
                            beg=i+1
                            break
                    s=geti(fp)

                if not s:
                    log.error("Malformed string, comments not ended by */ ")   
                    return None
        elif s==Apostrophe:
            s=geti(fp)
            while s and s!=Apostrophe:
                if s>0 and s<32:
                    if s==Newline:
                        ++common.counter
                    res+=buff[beg:i]
                    beg=i
                s=geti(fp)

            if not s:
                log.error("Malformed string, odd number of '")   
                return None

        s=geti(fp)

    if not s:
        log.error("Malformed string, odd number of '")   
        return None;

    if beg<i:
        res+=buff[beg:i]
    return res


def parseList(s):
    """parse the string s and return a list of args
        example:
            input: (#1,#3),#2           
            output:['(#1,#3)','#2']
    """
    beg=0
    i=0
    brackets=0
    res=[]
    while i<len(s):
        if ord(s[i])==Apostrophe:#'
            try:
                i=s.index(chr(Apostrophe),i+1)
            except Exception :
                log.error("Malformed string, odd number of  ' ")
                return None
        elif ord(s[i])==LeftParenthesis:
            brackets+=1
        elif ord(s[i])==RightParenthesis:
            if brackets==0:
                log.error("Brackets not match")
                return None
            else:
                brackets-=1
        elif ord(s[i])==Comma and brackets==0:
            res.append(s[beg:i])
            beg=i+1
        i+=1

    if beg<i:
        res.append(s[beg:i])
    if brackets>0 :
        log.error("Brackets not match")
        return None

    return res

    
def getIdParam(s):
    """return int value of a id param
        example :
            input :#4
            return 4
    """
    if ord(s[0])==DollarSign:
        return [ID_UNSET]
    try:
        res=int(s[1:])
    except Exception:
        return [ID_UNDEF]
    return [res]

def getSubParameter(arg,func):
    """ get a parameter from a sub parameter
        func:function to deal with value
        example: 
            input:"(.1,.2)"
            output:['.1','.2']      
    """
    if len(arg)<3 or arg[0]!='(' or arg[-1]!=')':
        return None

def fromSPF(string):
    """"""
    return string[1:-1] if string[0]=="'" or string[0]=="\"" else string

def strToSPF(string):
    """"""
    return '$' if string==None else "'%s'"%string

def spfToInteger(string):
    """"""
    try:
        return int(string)
    except:
        return float(string)

def integerToSPF(integer):
    """"""
    if integer==None:
        return '$'
    res=str(integer)
    return res if len(res)==1 else res.rstrip('0')
    

def spfToLogical(string):
    """"""
    string=string.upper()
    if string=='.F.':
        return False
    elif string=='.T.':
        return False
    else:
        return UNKNOWN

def logicalToSPF(logical):
    """"""
    if logical==None:
        return '$'
    if logical==True:
        return '.T.'
    elif logical==False:
        return '.F.'
    else:
        return '.U.'

def spfToBinary(string):
    """"""
    return string

def binaryToSPF(binary):
    """"""
    return '$' if binary==None else binary
    
def spfToId(string):
    """"""
    return int(string[1:])

def idToSPF(idx):
    """"""
    return '$' if idx==None else '#%d'%idx
    
def spfToTypeRef(string):
    """"""
    return string

def typerefToSPF(typeref):
    """"""
    return '$' if typeref==None else  typeref

def isUnset(arg):
    """"""
    return arg=='$' or arg=='*'

def getIdListParam(s,func=spfToId):
    """ return a list of the list type param
        func
        example:
        input:'(#1,#3)'
        output:[1,3]
    """ 

    res=[]
    if ord(s[0])==DollarSign:
        #res.append(ID_UNSET)
        return None

    if len(s)<3 or s[0]!='(' or s[-1]!=')':
        return res

    ids=parseList(s[1:-1])
    if not ids:
        res.append(ID_UNSET)
        return res
    else:
        for i in ids:
            try:
                #deal with value
                current=func(i)
            except Exception:
                res.append(ID_UNDEF)
                return res
            res.append(current)
        return res

def listParamToSPF(args,func=idToSPF):
    """"""
    if args==None:
        return '$'
    params=['%s'%func(i) for i in args]
    return '(%s)'%(','.join(params))


def render(templName,args,to=None,append=False):
    """"""
    templName=templName.lower()
    if templName in templCache:
        code=templCache[templName]
    else:
        HERE = os.path.dirname(os.path.abspath(__file__))
        templPath=os.path.join(HERE,"templates/%s"%templName).replace('\\','/')
        with open(templPath,'r') as fp:
            if not fp:
                log.error("templates/%s not found"%templName);
                return
            code=fp.read()
        templCache[templName]=code

    #replace
    p=re.compile(r"\{.+?}")
    pos=p.search(code)
    while pos:
        ops=pos.group()[1:-1].split('|')
        if len(ops)<1:
            log.error("Argument in template %s is empty."%templName)
            break
        key=ops[0]
        if not key in args:
            log.error("Argument %s in template %s not supplied."%(key,templName))
            break
        arg=str(args[key])
        #ops
        del(ops[0])
        for op in ops:
            if op.lower()=='title':  
                arg=arg.title()
            elif op.lower()=='upper':  
                arg=arg.upper()
            elif op.lower()=='lower':  
                arg=arg.lower()
        #replace
        code=code[:pos.start()]+arg+code[pos.end():]
        pos=p.search(code)

    #render to
    if not to:
        return code
    to=to.lower()
    flag='a' if append else 'w'

    with open(to,flag) as fp:
        if not fp:
            log.error("%s cannot be created or opend"%to);
            return 
        fp.write(code)

def getList(values,hasId=False,hasCommer=False):
    """"""
    code=''    
    if hasId:
        idx=0
        fmt='    %s=%d,\n' if hasCommer else '    %s=%d\n'
        for value in values:
                code+=fmt%(value.strip(),idx)
                idx+=1
    else :
        for value in values:
            fmt='    %s,\n' if hasCommer else '    %s\n'
            code+=fmt%value.strip()
    return code

 
def CalcSha1(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash
 
def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash

