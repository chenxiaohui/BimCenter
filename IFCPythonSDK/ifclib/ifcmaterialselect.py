#!/usr/bin/python
#coding=utf-8
#Filename:IfcMaterialSelect.py

#TYPE IfcMaterialSelect = SELECT
	#(IfcMaterial,IfcMaterialList,IfcMaterialLayerSetUsage,IfcMaterialLayerSet,IfcMaterialLayer);
#END_TYPE;

class IfcMaterialSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcMaterialSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        
