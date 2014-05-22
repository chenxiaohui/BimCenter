#!/usr/bin/python
#coding=utf-8
#Filename:expressionparser.py

class ExpressionParser(object):
    """"""
    def __init__(self,clause):
        super(ExpressionParser,self).__init__()
        self.clause=clause
        self.i=0

    def parse(self):
        """"""
        where=[]

        where.append(self.parseSingleExp())
        token=self.geti()
        while token:
            exp=self.parseSingleExp()
            if token=='and':
                pass
            elif token=='or':
                pass
            where.append(exp)
            token=self.geti()

        return where

    def parseSingleExp(self):
        key=self.geti()
        op=self.geti()
        value=self.geti()
        if value[0]=="'" and value[-1]=="'":
            value=value[1:-1]
        else:
            try:
                value= int(value)
            except:
                value= float(value)
        return [key,op,value]


    def isBlank(self):
        """"""
        return self.clause[self.i]==' ' or self.clause[self.i]=='\t'

    def isOp(self):
        """"""
        return self.clause[self.i] in ['<','>','=','!']

    def isSep(self):
        return self.clause[self.i] in ['(',')']

    def isEnd(self):
        """"""
        return self.i>=len(self.clause)

    def geti(self):
        """ symbol:
            = > < != >= <=
            and or ()
        """
        if self.isEnd():
            return None
        #omit blanks and tabs
        if self.isBlank():
            self.i+=1
            if self.isEnd():
                return None
            while self.isBlank():
                if self.isEnd():
                    return None
                self.i+=1

        if self.isOp():
            beg=self.i
            if self.clause[self.i+1]=='=':
                self.i+=2
            else:
                self.i+=1
            return self.clause[beg:self.i]
        elif self.isSep():
            beg=self.i
            self.i+=1
            return self.clause[beg:self.i]
        beg=self.i
        while not self.isEnd() and not self.isBlank() and not self.isOp():#end
            self.i+=1
        return self.clause[beg:self.i]
