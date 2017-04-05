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
  class PowerString(str):
    #def __new__(cls, strval):
      #ob = super(PowerString, cls).__new__(cls, string)
      #vout = self
      #return vout
      #self.strval = str(strval)
      #return str.__new__(cls, value)
      #return

    def __init__(self, strval=None, ddata=None ):
      if strval is None:
        self.strval = ""
      elif (True):
        self.strval = strval

      if ddata is None:
        self.ddata = {}
      elif (True):
        self.ddata = ddata
    ##;;

    def title(self):
      self.strval = str(self.strval).title()
      return self
    ##;;

    def reverse(self):
      self.strval = str(self.strval)[::-1]
      return self
    ##;;

    def render(self):
      vout = super(PowerString, self).title()
      return str(self.strval)
    ##;;

    def __getattr__(self, name):
      def _missing(*args, **kwargs):
        print "A missing method was called."
        print "The object was %r, the method was %r. " % (self, name)
        print "It was called with %r and %r as arguments" % (args, kwargs)
      return _missing
      #return self
    ##;;

if(not not 'py_demo_process'):
  mytest =  PowerString("hello world").reverse().title().render()
  print mytest
  pass

if(not 'py_demo_process'):
  mytest =  PowerString("hello world").render()
  print mytest
  pass

if(not 'py_demo_process'):
  PowerString("hello world").noexisto(1,2,*[3,4,5],**{'1':'1'})



