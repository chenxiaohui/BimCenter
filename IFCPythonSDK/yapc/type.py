#!/usr/bin/python
#coding=utf-8
#Filename:type.py
from serializable import Serializable
BASETYPE=['NUMBER','INTEGER','REAL','LOGICAL','BOOLEAN','BINARY','STRING']
AGGREGATIONTYPE=['BAG','LIST','ARRAY','SET']

class Type(Serializable):
    """"""
    def __init__(self):
        super(Type,self).__init__()

    def merge(self,ty):
        """ merge a type and it's ref type
        """
        pass
        #self.content=dict(self.content,**ty.content)
        #if self['TYPE'] in BASETYPE:
            

#class ComplexType(Type):
    #def __init__(self):
        #super(ComplexType,self).__init__()
        #self.name="complex"

#from json import JSONEncoder
#class MyEncoder(JSONEncoder):
    #def default(self, o):
        #return o.__dict__    

#ty1= Type()
#ty1.content= { "VALUES": [ "IfcOrganization", "IfcPerson", "IfcPersonAndOrganization" ], "TYPE": "SELECT" }
#ty2=Type()
#ty2.content= { "TYPE": "IfcAssemblyPlaceEnum" }
#ty2.where={ "WR1": "SELF IN [ 'top-left' , 'top-middle' , 'top-right' , 'middle-left' , 'center' , 'middle-right' , 'bottom-left' , 'bottom-middle' , 'bottom-right' ]" } 
#ty1.merge(ty2)
#print ty1.Serialize()
