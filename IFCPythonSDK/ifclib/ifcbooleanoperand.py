#!/usr/bin/python
#coding=utf-8
#Filename:IfcBooleanOperand.py

#TYPE IfcBooleanOperand = SELECT
	#(IfcSolidModel,IfcHalfSpaceSolid,IfcBooleanResult,IfcCsgPrimitive3D);
#END_TYPE;

class IfcBooleanOperand(object):
    """"""
    def __init__(self,obj):
        super(IfcBooleanOperand,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        
