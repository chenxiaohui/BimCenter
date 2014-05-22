#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralActivityAssignmentSelect.py

#TYPE IfcStructuralActivityAssignmentSelect = SELECT
	#(IfcStructuralItem,IfcElement);
#END_TYPE;

class IfcStructuralActivityAssignmentSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcStructuralActivityAssignmentSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        
