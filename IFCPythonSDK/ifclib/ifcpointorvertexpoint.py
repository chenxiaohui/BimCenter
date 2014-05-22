#!/usr/bin/python
#coding=utf-8
#Filename:IfcPointOrVertexPoint.py

#TYPE IfcPointOrVertexPoint = SELECT
	#(IfcPoint,IfcVertexPoint);
#END_TYPE;

class IfcPointOrVertexPoint(object):
    """"""
    def __init__(self,obj):
        super(IfcPointOrVertexPoint,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        
