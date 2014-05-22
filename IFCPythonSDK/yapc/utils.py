#!/usr/bin/python
#coding=utf-8
#Filename:utils.py
import common
import log
import re
import config

symbol=[',','=',';',':','{','}','(',')','[',']','<','>']
end=[' ','\n','\r','\t']
#lastpos={}
lastpos=0
templCache={}

def geti(fp):
    """
        symbol table: 
        , = ; : { } [ ] ( ) ? word :=
        comment(**)
    """
    global symbol,end,lastpos
    word=''
    #lastpos[id(fp)]=fp.tell()
    lastpos=fp.tell()
    s=fp.read(1)
    if s in symbol:#just a special symbol
        #[:|>|<]= return together
        if s in [':','>'] :
            t=fp.read(1)
            if t=='=':
                return s+t
            elif t:
                fp.seek(-1,1)
        elif s=='<':
            t=fp.read(1)
            if t=='=' or t=='>':
                return s+t
            elif t:
                fp.seek(-1,1)
        elif s=='(':#comment
            t=fp.read(1)
            if t=='*':
                skipComment(fp)
                return geti(fp)
            elif t:
                fp.seek(-1,1)
        return s

    elif s in end:#end symbol,omit it to the first no-end symbol
        if s=='\n':
            common.counter+=1

        s=fp.read(1)
        while s in end:
            if s=='\n':
                common.counter+=1
            s=fp.read(1)
        #go back one char
        if s:
            fp.seek(-1,1)
        return geti(fp)
    else:
        while s and not s in end and not s in symbol:
            word+=s
            s=fp.read(1)

        #go back one char
        if s:
            fp.seek(-1,1)
        return word

def back(fp):
    """go back one word
    """
    #fp.seek(lastpos[id(fp)])
    fp.seek(lastpos)

def close(fp):
    """"""
    #global lastpos
    #del lastpos[id(fp)]
    fp.close()

def skipComment(fp):
    s=fp.read(1)    
    while s:
        if s=='*':
            t=fp.read(1)
            if t==')':#end of comment
                break
        s=fp.read(1)


def render(templName,args,to=None,append=False):
    """"""
    templName=templName.lower()
    if templName in templCache:
        code=templCache[templName]
    else:
        with open("templates/%s.py"%templName,'r') as fp:
            if not fp:
                log.error("templates/%s.py not found"%templName);
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

    with open('../'+config.get('lib','name')+'/%s.py'%to,flag) as fp:
        if not fp:
            log.error("file codes/%s.py cannot be created or opend"%to);
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

#if __name__ == '__main__':
    #with open('IFC2X3_TC1.exp','rb') as fp:
    #fp=open('test.in','rb')
    #print geti(fp)
    #print geti(fp)
    #print geti(fp)
    #print lastpos
    #close(fp)

    #try:
        #import cStringIO as StringIO
    #except Exception :
        #import StringIO
    #s = StringIO.StringIO("sss(* is a handsome a*)")
    #print geti(s)
    #back(s)
    #print geti(s)
    #print geti(s)
    #print geti(s)
