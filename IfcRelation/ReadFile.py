#!/usr/bin/python
#Filename:ReadFile.py

def read(filename):
    try:
        fp=open(filename,"r") 
    except Exception, e:
        raise e
    res={}
    while True:
        str=fp.readline().strip("\n")
        if len(str)==0:
            break
        elif str[0]!='#':
            continue
        line=[]
        pos=str.find("=")#find=
        end=str.find("(")
        #print pos,end
        line.append(str[pos+1:end])
        line.append(str[end:])
        res[str[1:pos]]=line[:]
    return res
