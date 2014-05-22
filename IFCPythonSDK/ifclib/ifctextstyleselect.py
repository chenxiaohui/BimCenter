#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextStyleSelect.py

#TYPE IfcTextStyleSelect = SELECT
	#(IfcTextStyleWithBoxCharacteristics,IfcTextStyleTextModel);
#END_TYPE;

class IfcTextStyleSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcTextStyleSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        
