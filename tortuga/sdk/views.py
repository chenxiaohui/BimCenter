# Create your views here.

import os
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.conf import settings
from forms import ModelUploadForm,SRLUploadForm,SRLChooseForm
from models import Indexes,SRL
from ifc import CalcHash,parseIFC,deleteModelVersion,toSubModel
from django.db import connection

def direct(request, template_name):
    return render_to_response(template_name, {})
    
def modelsView(request):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT  model_id as id ,count(model_id) as cnt FROM sdk_indexes group by model_id;
        """)

    desc = cursor.description 
    models= [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]
    print models
    return render_to_response('models.html',{'models':models})
    
def srlsView(request):
    if request.method=='POST':
        form=SRLUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/srls/')
    else:
        form=SRLUploadForm()
        srls=SRL.objects.all()
        return render_to_response('srls.html',{'form':form,'srls':srls})

def modelView(request,mid):
    if request.method=='POST':
        form=ModelUploadForm(request.POST,request.FILES)
        
        if form.is_valid():
            fp=form.cleaned_data['file']
            hash=CalcHash(fp)
            ifcpath=os.path.join(settings.MEDIA_ROOT,'files').replace('\\','/')
	    filepath=os.path.join(ifcpath,str(mid)).replace('\\','/')
            if not os.path.exists(filepath):
                os.mkdir(filepath)               
            filename=os.path.join(filepath,hash+'.ifc').replace('\\','/')
            if os.path.exists(filename):
                return HttpResponse('has exists')

            dest = open(filename, 'wb')
            for chunk in fp.chunks():
                dest.write(chunk)
            dest.close()
            
            parseIFC(filename,hash,mid)
        return HttpResponseRedirect('/model/%s/'%mid)
    else:
        form=ModelUploadForm()
        versions=Indexes.objects.filter(model_id=mid)
        return render_to_response('model.html',{'mid':mid,'form':form,'versions':versions})

        #form=IndexForm(request.POST,request.FILES)
        #if form.is_valid():
            #model=form.save(commit=False)
            #model.hash=CalcHash(model.file)
            #model.save()

def deleteView(request,mid,version=None):
    """"""            
    ifcpath=os.path.join(settings.MEDIA_ROOT,'files').replace('\\','/')
    filepath=os.path.join(ifcpath,str(mid)).replace('\\','/')
    if version:
        version=float(version)
        idx=Indexes.objects.filter(model_id=mid,version=version)
        if idx:
            filename=os.path.join(filepath,idx[0].hash+'.ifc').replace('\\','/')
        os.remove(filename)
    else:
        idxs=Indexes.objects.filter(model_id=mid)
        print idxs
        if idxs:
            for idx in idxs:
                filename=os.path.join(filepath,idx.hash+'.ifc').replace('\\','/')
                os.remove(filename)
            os.rmdir(filepath)
    deleteModelVersion(int(mid),version)
    return HttpResponseRedirect('/model/%s/'%mid)

def versionView(request,mid,verId):
    """"""
    try:
        version=Indexes.objects.filter(model_id=mid,version=verId)[0]
    except Exception :
        raise Http404

    if request.method=='POST':
        form=SRLChooseForm(request.POST)
        if form.is_valid():
            srlId=form.cleaned_data['srl']
            try:
                srl=SRL.objects.filter(id=srlId)[0]
            except Exception:
                raise Http404
            #print srl.file,version.hash
            srlfilename=os.path.join(settings.MEDIA_ROOT,srl.file.name).replace('\\','/')
            subContent=toSubModel(srlfilename,version.hash)
            if subContent:
                subResponse=HttpResponse(subContent,mimetype="application/octet-stream")
                subResponse['Content-Disposition'] = 'attachment; filename=submodel.ifc'
                return subResponse
    else:
        form=SRLChooseForm()
    return render_to_response('version.html',{'srlform':form,'version':version,'mid':mid})
