#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

""" Dictionary to XML - Library to convert a python dictionary to XML output
    Copyleft (C) 2007 Pianfetti Maurizio <boymix81@gmail.com>
    Package site : http://boymix81.altervista.org/files/dict2xml.tar.gz

    Revision 1.1.0  2012/07/22 17:55:34  Maurizio, Thomas 
    - Add Encoding parameter

    Revision 1.0  2007/12/15 11:57:20  Maurizio
    - First stable version

"""

__author__ = "Pianfetti Maurizio <boymix81@gmail.com>"
__contributors__ = ["Thomas Fossoul <fossoul.t@gmail.com>"]
__date__    = "$Date: 2012/07/22 17:55:34  $"
__credits__ = """..."""
__version__ = "$Revision: 1.1.0 $"

class Dict2XML:
    #XML output
    xml = ""

    #Tab level
    level = 0

    #Encoding
    encoding = ""

    def __init__(self):
        self.xml = ""
        self.level = 0
    #end def

    def __del__(self):
        pass
    #end def

    def setXml(self,Xml):
        self.xml = Xml
    #end def

    def setLevel(self,Level):
        self.level = Level
    #end def

    def setEncoding(self,Encoding):
        self.encoding = Encoding
    #end def
    
    def stringEncoded(self,strIn):
        if self.encoding != "":
            return  strIn.encode(self.encoding)
        else:
            return strIn
    #end def
    
    def dict2xml(self,map):
        if (str(type(map)) == "<class 'object_dict.object_dict'>" or str(type(map)) == "<type 'dict'>"):
            for key, value in map.items():
                key = self.stringEncoded(key)
                if (str(type(value)) == "<class 'object_dict.object_dict'>" or str(type(value)) == "<type 'dict'>"):
                    if(len(value) > 0):
                        self.xml += self.stringEncoded("\t"*self.level)
                        self.xml += self.stringEncoded("<%s>\n" % (key))
                        self.level += 1
                        self.dict2xml(value)
                        self.level -= 1
                        self.xml += self.stringEncoded("\t"*self.level)
                        self.xml += self.stringEncoded("</%s>\n" % (key))
                    else:
                        self.xml += self.stringEncoded("\t"*(self.level))
                        self.xml += self.stringEncoded("<%s></%s>\n" % (key,key))
                    #end if
                else:
                    self.xml += self.stringEncoded("\t"*(self.level))
                    self.xml += self.stringEncoded("<%s>%s</%s>\n" % (key,self.stringEncoded(value), key))
                #end if
        else:
            self.xml += self.stringEncoded("\t"*self.level)
            self.xml += self.stringEncoded("<%s>%s</%s>\n" % (key,self.stringEncoded(value), key))
        #end if
        return self.xml
    #end def

#end class

def createXML(dict,xml,encoding = ''):
    xmlout = Dict2XML()
    xmlout.setXml(xml)
    xmlout.setEncoding(encoding)
    return xmlout.dict2xml(dict)
#end def

dict2Xml = createXML

if __name__ == "__main__":

    #Define the dict
    d={}
    d['root'] = {}
    d['root']['v1'] = "";
    d['root']['v2'] = "hi";
    d['root']['v3'] = {};
    d['root']['v3']['v31']="hi";

    #xml='<?xml version="1.0"?>\n'
    xml = ""
    print dict2Xml(d,xml)
    
    print "Encoding.."
    enc = "iso-8859-15"
    d={}
    d['root'] = {}
    
    xml = ""
    print dict2Xml(d,xml,enc)
    

#end if
