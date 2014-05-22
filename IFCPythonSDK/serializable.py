#!/usr/bin/python
#coding=utf-8
#Filename:Serializable.py
import json
#exempt=['lid','args','binited','expDataSet','type']
exempt=['lid','args','binited','expDataSet']

class Serializable(object):
    """"""
    def __init__(self):
        super(Serializable,self).__init__()

    def Serialize(self):
        """"""
        return json.dumps(
            {key:value for key,value in self.__dict__.items() if key not in exempt},
            sort_keys=True,
            indent=4,
            ensure_ascii=False
            )

    def toDict(self):
        """"""
        return {key:value for key,value in self.__dict__.items() if key not in exempt}        
    def toCode(self):
        """"""
        return '#%d=%s(%s);'%(self.lid,self.type,self.toString().strip(","))

    def Construct(self,metadata):
        for key,value in metadata.items():
            self.__dict__[key]=value
