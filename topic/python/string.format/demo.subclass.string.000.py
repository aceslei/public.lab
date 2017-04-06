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
###     lastupdate: "__lastupdate__"
###     desc: |
###         * __desc__
###     seealso: |
###         * __seealso__
### <end-file_info>
"""

if('py_init_class'):
  class PyHereDoc(object):
    def __init__(self, strval=None, ddata=None ):
      self.strval = strval  if bool(strval) else ""
      self.ddata  = ddata   if bool(ddata) else {}
    ##;;

    def anonop(self,*args): return self
    def render(self): return str(self.strval)
    def reverse(self): self.strval = str(self.strval)[::-1];
      return self
    ##;;

    def __str__(self):
      return self.render()
    ##;;

    def __getattr__(self, name):
      ##
      try:
        self.strval = getattr(str,name)(self.strval)
        return self.anonop
      except Exception: pass
      ##
      return self.anonop
    ##;;

if('demo_holdingsqpalan'):
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

if(not 'demo_holdingsqlalan'):
  ## all of these work as expected and desired
  print PyHereDoc("hello world").upper().reverse().render()
  pass

if( 'demo_holdingsqmalan'):
  ## all of these work as expected and desired
  pass

if( 'demo_holdingsqnalan'):
  ## all of these work as expected and desired
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
