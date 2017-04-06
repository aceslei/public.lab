# -*- coding: utf-8 -*-
"""
### <beg-file_info>
### document_metadata:
###   - caption: "__blank__"
###     dmid: "demo_subclassstring_tilingqpsocket"
###     date: created="2017-04-05"
###     last: lastmod="2017-04-05"
###     tags: tags
###     author: created="__author__"
###     filetype: "yaml"
###     lastupdate: "puts-right is the default puts format"
###     desc: |
###         * __desc__
###     seealso: |
###         * __seealso__
### <end-file_info>
"""

if('init_python'):
  import re
  import string
  import textwrap
  import yaml

if('py_init_class'):
  class PyHereDoc(object):
    def __init__(self, strval=None, ddata=None, dconfig=None, ):
      self.strval = strval  if bool(strval) else ""
      self.ddata  = ddata   if bool(ddata)  else {}
    ##;;

    ##
    def anonop(self,*args):
      return self
    ##;;

    def fmtputs(self,sbody='',spec='',):
      sbeg = "\n"  if("<" in spec) else ""
      send = "\n"  if(">" in spec) else ""
      return "".join([sbeg,"{0}".format(str(sbody)),send])
    ##;;

    ##
    def strip(self,spec='<>'):
      '''
      Note: strip left ('<') removes newline at beginning of *entire string*,
          not the most recently concatted portion thereof
      '''
      if(">" in spec): self.strval = str(self.strval).rstrip()
      if("<" in spec): self.strval = str(self.strval).lstrip()
      return self
    ##;;

    def puts(self,spec='>'):
      '''
      Note: puts left ('<') puts newline at beginning of *entire string*,
          not the most recently concatted portion thereof
      '''
      self.strval = self.fmtputs(self.strval,spec)
      return self
    ##;;

    def concat(self,*args):
      aatemp = [str(self.strval)]
      aatemp.extend( str(vxx) for vxx in list(args) )
      self.strval = "".join( aatemp )
      return self
    ##;;

    def dedent(self):
      self.strval = textwrap.dedent(self.strval)
      return self
    ##;;

    def each(self,items=None,spec=None):
      self.strval = self.strval + str( "".join([
        self.fmtputs(str(vxx),str(spec))
        for vxx in items
        ]))
      return self
    ##;;

    def render(self):
      return str(self.strval)
    ##;;

    def reverse(self):
      self.strval = str(self.strval)[::-1];
      return self
    ##;;

    def __repr__(self):
      return self.render()
    ##;;

    def __getattr__(self, name):
      try:
        self.strval = getattr(str,name)(self.strval)
      except Exception: pass
      ##
      return self.anonop
    ##;;

if('demo_holdingsqlalan'):
  odata = yaml.safe_load('''
  - fname: Homer
    lname: Simpson
  - fname: Maggie
    lname: Bimpson
  - fname: Lisa
    lname: Dimpson
  ''')
  vout = ''
  vout += str(PyHereDoc(
          """
          Hello
          Hello
          Hello
          """)
          .dedent()
          .strip("<>")
          .puts('>')
          .concat(".there").puts()
          .concat(".world").puts()
          .concat("----").puts()
          .each(odata,'>')
          .concat("----").puts()
          .concat("----")
          )
  print vout
  pass

if(not 'demo_holdingsqpalan'):
  ## all of these work as expected and desired
  odata = dict()
  odata['fname'] = 'Homer'
  odata['lname'] = 'Simpson'
  print PyHereDoc("hello world")
  print PyHereDoc("hello world").reverse()
  print PyHereDoc("hello world").title().reverse()
  print PyHereDoc("hello world").reverse().title()
  print PyHereDoc("hello world").startswith('hello')
    ## this behaves differently when PyHereDoc extends object (keeps chainability)
    ## this behaves differently when PyHereDoc extends str (breaks chainability)
    ##    subclassing str breaks chainability because __getattr__ never gets called on `startswith`
    ##    since a `startswith` method exists on str
  pass


# if('demo002'):
#   print PyHereDoc("hello world").render()
#   print PyHereDoc("hello world").reverse().render()
#   print PyHereDoc("hello world").title().reverse().render()
#   print PyHereDoc("hello world").reverse().title().render()
#   pass

# if(not not 'py_demo_process'):
#   mytest =  PyHereDoc("hello world").reverse().title().render()
#   print mytest
#   pass
#
# if(not not 'py_demo_process'):
#   print type(PyHereDoc("hello world").upper)
#
# if(not 'py_demo_process'):
#   mytest =  PyHereDoc("hello world").reverse().title().render()
#   print mytest
#   pass

# if(not 'py_demo_process'):
#   print PyHereDoc("hello world").noexisto(1,2,*[3,4,5],**{'1':'1'})
