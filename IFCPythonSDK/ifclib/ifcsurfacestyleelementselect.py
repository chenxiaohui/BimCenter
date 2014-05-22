#!/usr/bin/python
#coding=utf-8
#Filename:IfcSurfaceStyleElementSelect.py

#TYPE IfcSurfaceStyleElementSelect = SELECT
	#(IfcSurfaceStyleShading,IfcSurfaceStyleLighting,IfcSurfaceStyleWithTextures,IfcExternallyDefinedSurfaceStyle,IfcSurfaceStyleRefraction);
#END_TYPE;

class IfcSurfaceStyleElementSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcSurfaceStyleElementSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        
