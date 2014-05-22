import os
import sys
import re
from submodel import SubModel
from utils import render

def toGraph(model,basename):
    """"""
    pattern=re.compile(r'#(\d+)')
    code=''
    for key,value in model.lines.items():
        #print key,value
        refs=pattern.findall(value[1])
        for ref in refs:
            code+='    %d->%s;\n'%(key,ref)
    title=model.header.fileName.name
    render('temp.dot',
           {'name':title,'content':code},
           basename+'.dot')

if __name__ == '__main__':
    if len(sys.argv)<2:
        print "Command Args error."
        print "Help: python graph.py <filename> [-o <filetype>]"
        exit()
    fname=sys.argv[1]
    if(len(sys.argv)>2 and sys.argv[2]=='-o'):
        ty=sys.argv[3]
    else:
        ty='png'

    fname=fname.replace(".ifc","")
    model=SubModel()
    with open(fname,'r') as fp:
        model.read(fp)

    toGraph(model,fname)

    print ('dot -T %s %s.dot -o %s.%s'%(ty,fname,fname,ty))
    os.system('dot -T %s %s.dot -o %s.%s'%(ty,fname,fname,ty))
    os.remove(fname+'.dot')
    os.system(fname.replace('/','\\')+'.'+ty)
