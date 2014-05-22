#!/usr/bin/python
#coding=utf-8
#Filename:IfcUnit.py

#TYPE IfcUnit = SELECT
	#(IfcDerivedUnit,IfcNamedUnit,IfcMonetaryUnit);
#END_TYPE;

class IfcUnit(object):
    """"""
    def __init__(self,obj):
        super(IfcUnit,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        
