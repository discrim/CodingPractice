# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:58:15 2020

@author: shiny
"""

def hashMap2(queryType, query):
    mymap = []
    ql = len(queryType)
    gets = 0
    for ii in range(ql):
        if queryType[ii] == 'insert':
            mymap.append(query[ii])
        elif queryType[ii] == 'get':
            for elem in mymap:
                if elem[0] == query[ii][0]:
                    gets += elem[1]
        elif queryType[ii] == 'addToKey':
            for elem in mymap:
                elem[0] += query[ii][0]
        elif queryType[ii] == 'addToValue':
            for elem in mymap:
                elem[1] += query[ii][0]
    return gets

def hashMap(queryType, query):
    keys = []
    vals = []
    ql = len(queryType)
    gets = 0
    for ii in range(ql):
        if queryType[ii] == 'insert':
            keys.append(query[ii][0])
            vals.append(query[ii][1])
        elif queryType[ii] == 'get':
            for key1 in keys:
                if key1 == query[ii][0]:
                    gets += vals[keys.index(key1)]
        elif queryType[ii] == 'addToKey':
            keys = [key1 + query[ii][0] for key1 in keys]
        elif queryType[ii] == 'addToValue':
            vals = [val1 + query[ii][0] for val1 in vals]
        print(keys)
        print(vals)
        print('\n')
    return gets

if __name__ == '__main__':
    qt1 = ["insert", "insert", "addToValue", "addToKey", "get"]
    qq1 = [[1, 2], [2, 3], [2], [1], [3]]
    print(hashMap(qt1, qq1))