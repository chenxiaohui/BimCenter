import ReadFile
import os
import sys
if len(sys.argv)<2:
    print "Command Args error."
    print "Help: python ifc.py <filename> [-o <filetype>]"
    exit()
fname=sys.argv[1]
if(len(sys.argv)>2 and sys.argv[2]=='-o'):
    ty=sys.argv[3]
else:
    ty='png'
res=ReadFile.read(fname.strip(".ifc")+".ifc")

#for key,value in res.items():
    #print key,value
dot=file(fname+".dot","w")
dot.write("digraph classic0{\n")
for key,value in res.items():
    #print key,value
    i=value[1].find('#')
    while i>-1:
        strleft=value[1][i+1:]
        j1=strleft.find(',')
        j2=strleft.find(')')
        j=min(j1,j2) if (j1>-1 and j2>-1) else max(j1,j2)
        dot.write(key+"->"+strleft[:j]+"\n")
        #print (key+"->"+strleft[:j]+"\n")

        value[1]=strleft[j:]
        i=value[1].find('#')
dot.write("}")
dot.close()
os.system('dot -T'+ty+' '+fname+'.dot -o '+fname+'.'+ty)
os.system(fname+'.'+ty)

