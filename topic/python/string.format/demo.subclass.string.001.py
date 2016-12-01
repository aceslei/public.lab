# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### main:
###   - date: created="Thu Dec 01 12:03:13 2016"
###     last: lastmod="Thu Dec 01 12:03:13 2016"
###     tags: python,string,format,subclass,oop,py2
###     author: created="dreftymac"
###     dmid: "narceine_land_brains"
###     filetype: "py"
###     lastupdate: "__lastupdate__"
###     desc: |
###         * demo code showing an alternate use of string.format()
###     seealso: |
###         * __seealso__
### <end-file_info>
'''

### ----------------------------------
if('init_python'):
  import re
  import yaml
  import textwrap
  from datetime import datetime

### ----------------------------------
if('init_custom_formatter'):
  class CustFmt(str):
    '''extend python str type to permit custom delimiters on str.format()
    '''
    def __new__(cls, value, srcdata={}, tkbeg='<%',tkend='%>',):
      return str.__new__(cls,value)
    def __init__(self,value,srcdata={}, tkbeg='<%',tkend='%>'):
      self.srcdata = srcdata;self.tkbeg = tkbeg;self.tkend = tkend;
    def myformat(self): return(self.__str__()
      .replace('{','{{').replace('}','}}')
      .replace(self.tkbeg,'{').replace(self.tkend,'}')
      .format(**self.srcdata))

### ----------------------------------
if('show_demo_usage::curly-brace-collisions-fixed'):

  odata   =   dict({"template":'string'})
  vout    =   CustFmt('''
  This is a <%template%> this is a {template}
  ''',odata).myformat()
  print vout

### ----------------------------------
if('show_demo_usage::fill-in-the-blank-document-generation'):


  ### ------------------------------------------------------------------------
  odata   =   yaml.safe_load('''
      username:   tvt173
      userid:     701803
  ''')

  ### ------------------------------------------------------------------------
  vout    =   CustFmt('''
  ## Overview

  This is an introductory document written to <%username%> from Dreftymac.

  ### Introduction


  Greetings!  I noticed you are a user on Stackoverflow!

  Your user page is located here:

  http://stackoverflow.com/users/<%userid%>/<%username%>

  Thanks for using the site! We programmers need to stick together! ^_^

  ''',odata).myformat()
  print vout
