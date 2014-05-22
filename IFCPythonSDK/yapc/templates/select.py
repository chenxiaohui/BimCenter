#!/usr/bin/python
#coding=utf-8
#Filename:{name}.py

#TYPE {name} = SELECT
	#({selectlist});
#END_TYPE;

class {name}(object):
    """"""
    def __init__(self,obj):
        super({name},self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        
