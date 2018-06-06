#!/usr/bin/env python
#-*- utf-8 -*-
#
# This script is used for implicit
# Created on May 6, 2013 by Ma Libo
#
# Updated History
# Ambiguous matching supported. updated @2014.6.3
#    mode 0 for exact mathcing fields separated by +
#    mode 1 for ambiguous matching files separated by , or whitespace
#    mode 2 for Invert matching updated@2016.8.18

import model
import re
import web
import sys
from config.settings import *
from hosts import isactived

unsupportchar='''@%^_-:;./\\'''

def quick_search(keyword,CASEIGNORE=True):
    ''' This fuction is used to fetch id number with keyword'''
    ids=[]

    if CASEIGNORE:
        kw=ignore_rec(keyword)
    else:
        kw=re.compile(keyword)

    data=model.get_entries()

    for i in data:
        for item in i.itervalues():
            item=str(item)
            result=re.search(kw,item)

            if result:
                if i.id not in ids:
                    ids.append(i.id)
            #list(set(ids)) # simple way to uniq elments in the id list.
    return ids


def advance_search(kw, mode=0):
    # Advance mode for filtering record
    '''
        mode = 0 means exact matching , keyword must exact match in the string
        mode = 1 means Ambiguous , just only matched the string will be returned.
        mode = 2 means Invert-matching.
    '''
    ids = []
    data=model.get_entries()

    for i in data:
        # Load data and convert into string.
        string=" ".join([str(item) for item in i.itervalues()])

        # Print string
        for k in kw.keys():
            kw[k]=_filter(k, string)

        if mode == 0:
            # Exact matching
            if False in kw.values():
                #print kw,i.hostname
                continue
            else:
                #if i.id not in ids:
#                print i.hostname
#                print kw,i.hostname
                ids.append(i.id)

        elif mode == 1:
            # Ambiguous matching
            if True in kw.values():
                ids.append(i.id)

        elif mode == 2:
            # Invert matching
            if False in kw.values():
                ids.append(i.id)
    return ids

def ignore_rec(keyword):
    return re.compile(keyword, re.IGNORECASE)

def _filter(keyword, string, mode=0):

    kw=re.compile(keyword,re.IGNORECASE)

    rst=re.search(kw, string)
    if rst:
        return True
    else:
        return False

def change_into_dict(list):
    "This function is used to change the input keyword for _filter"
    dic_data={}
    for i in list:
        dic_data[i]=False

    return dic_data


class Search:

    def GET(self):
        if isactived():
            status=True
        else:
            status=False
        data=web.input()
        keyword=data.search_body

        try:
            keyword=keyword.replace(unsupportchar," ")
        except Exception, e:
            print "%s, exception occured."%e
            return None

        if keyword.find("+") != -1:
            "Advance search mode "
            keyword=change_into_dict(keyword.split("+"))
            # print keyword
            ids=advance_search(keyword)

        elif keyword.find(",") != -1 or keyword.find(" ") != -1:
            # Convert "," into whitespace
            keyword=change_into_dict(re.split("[ |,]", keyword))
            ids=advance_search(keyword, mode=1)

        elif keyword.find("!") != -1:
            # Invert matching
            keyword=change_into_dict(keyword.split("!"))
            ids=advance_search(keyword, mode=2)

        else:
            ids=quick_search(keyword)

        if isinstance(ids,list):
            search_results=[]
            for id in ids:
                search_results.append(model.get_entry(id))
            return render.search(search_results, status)

