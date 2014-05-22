#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceOrFaceSurface.py

#TYPE IfcSurfaceOrFaceSurface = SELECT
	#(IfcSurface,IfcFaceSurface,IfcFaceBasedSurfaceModel);
#END_TYPE;

class IfcSurfaceOrFaceSurface(object):
    """"""
    def __init__(self,obj):
        super(IfcSurfaceOrFaceSurface,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        
