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
  class PowerString(object):
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

    def aanoop(self,*args):
      print args
      self.strval = self.strval
      return self
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
      return str(self.strval)
    ##;;

    def __str__(self):
      return self.render()
    ##;;

    def __getattr__(self, name):
      ##
      try:
        self.strval = getattr(str,name)(self.strval)
      except Exception: pass
      ##
      return self.aanoop
    ##;;

    # def __getattr__(self, name):
    #   if(True):
    #     self.strval = getattr(str,name)(self.strval)
    #     #return self.__new__(self.strval,self.ddata)
    #   elif(True):
    #     def _missing(*args, **kwargs):
    #       print "A missing method was called."
    #       print "The object was %r, the method was %r. " % (self, name)
    #       print "It was called with %r and %r as arguments" % (args, kwargs)
    #     return _missing
    #   #return self
    # ##;;

if('demo_holdingsqpalan'):
  ## all of these work as expected and desired
  print PowerString("hello world")
  print PowerString("hello world").reverse()
  print PowerString("hello world").title().reverse()
  print PowerString("hello world").reverse().title()
  print PowerString("hello world").startswith('hello')
  pass

if(not 'demo_holdingsqlalan'):
  ## all of these work as expected and desired
  print PowerString("hello world").upper().reverse().render()
  pass

if( 'demo_holdingsqmalan'):
  ## all of these work as expected and desired
  pass

if( 'demo_holdingsqnalan'):
  ## all of these work as expected and desired
  pass


# if('demo002'):
#   print PowerString("hello world").render()
#   print PowerString("hello world").reverse().render()
#   print PowerString("hello world").title().reverse().render()
#   print PowerString("hello world").reverse().title().render()
#   pass

# if(not not 'py_demo_process'):
#   mytest =  PowerString("hello world").reverse().title().render()
#   print mytest
#   pass
#
# if(not not 'py_demo_process'):
#   print type(PowerString("hello world").upper)
#
# if(not 'py_demo_process'):
#   mytest =  PowerString("hello world").reverse().title().render()
#   print mytest
#   pass

# if(not 'py_demo_process'):
#   print PowerString("hello world").noexisto(1,2,*[3,4,5],**{'1':'1'})
