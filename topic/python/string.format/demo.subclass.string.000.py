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
###     lastupdate: "clean up heredoc demo to minimize method calls"
###     desc: |
###         * __desc__
###     seealso: |
###         * http://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string
### <end-file_info>

## TODO: todoitems_securelyqpstash
  * TODO ;; add in CustomFormat with placeholder syntax
  * TODO ;; methods to add
      * tofile()
      * tozipfile()
      * possible chainable formatters in customized str.formatter?
  * TODO ;; make option for default fmtbody args, to reduce linenoise
      * <img src="data:image/png;base64,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" />

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
      self.ddata  = ddata   if bool(ddata)  else []
    ##;;

    ### ------------------------------------------------------------------------

    ##
    def anonop(self,*args):
      return self
    ##;;

    ### ------------------------------------------------------------------------

    def fmtbody(self,sbody=None,**kwargs):
      bdedent = bool(kwargs['dedent'])if ('dedent' in kwargs) else False
      iindent = int(kwargs['indent']) if ('indent' in kwargs) else -1
      sstrip  = str(kwargs['strip'])  if ('strip' in kwargs)  else ""
      sputs   = str(kwargs['puts'])   if ('puts' in kwargs)   else ""
      schomp  = str(kwargs['chomp'])  if ('chomp' in kwargs)  else ""
      sbody   = str(sbody)            if (not sbody is None)  else ""
      if(bdedent or iindent > -1):  sbody = textwrap.dedent(sbody)
        ## TODO: decide whether you want this
        ## dedent is implicit when indent is present and gt neg1
      if(sstrip):   sbody = self.fmtstrip(sbody,sstrip)
      if(schomp):   sbody = self.fmtchomp(sbody,schomp)
      if(sputs):    sbody = self.fmtputs(sbody,sputs)
      if(iindent > -1): sbody = self.fmtindent(sbody,iindent)
      return sbody
    ##;;

    def fmtchomp(self,sbody='',spec='',):
      if("<" in spec): sbody = str(sbody).rstrip()
      if(">" in spec): sbody = re.sub(r'\n$','',str(sbody))
      return sbody
    ##;;

    def fmtindent(self,sbody='',isize='0',):
      isize = int(isize)
      if(int(isize)>-1):
        aabody    = sbody.splitlines()
        aabody    = [(isize * ' ') + line + "\n" for line in aabody]
        sbody     = ''.join(aabody)
      return sbody
    ##;;

    def fmtputs(self,sbody='',spec='',):
      sbeg = "\n"  if("<" in spec) else ""
      send = "\n"  if(">" in spec) else ""
      return "".join([sbeg,"{0}".format(str(sbody)),send])
    ##;;

    def fmtstrip(self,sbody='',spec='',):
      if(">" in spec): sbody = str(sbody).rstrip()
      if("<" in spec): sbody = str(sbody).lstrip()
      return sbody
    ##;;

    ##
    def strip(self,spec='<>'):
      '''
      Note: strip left ('<') removes newline at beginning of *entire string*,
          not the most recently concatted portion thereof
      '''
      self.strval = self.fmtstrip(self.strval,spec)
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

    ### ------------------------------------------------------------------------

    def concat(self,sbody=None,**kwargs):
      sbody       = str(sbody) if (not sbody is None) else "_blank_"
      sputs       = str(kwargs['puts']) if ('puts' in kwargs) else ""
      sstrip      = str(kwargs['strip']) if ('strip' in kwargs) else ""
      odata       = (kwargs['data'])     if ('data' in kwargs) else None
      if(False):  pass
      elif( odata ):
        self.strval += self.fmtbody(sbody.format(**odata),**kwargs)
      elif( not odata ):
        self.strval += self.fmtbody(str(sbody),**kwargs)
      return self
    ##;;

    def dedent(self):
      self.strval = textwrap.dedent(self.strval)
      return self
    ##;;

    def each(self,sbody=None,**kwargs):
      sbody       = str(sbody) if (not sbody is None) else "{0}"
      sputs       = str(kwargs['puts']) if ('puts' in kwargs) else ""
      sstrip      = str(kwargs['strip']) if ('strip' in kwargs) else ""
      odata       = (kwargs['data'])     if ('data' in kwargs) else self.ddata
      self.strval = self.strval + str( "".join([
        self.fmtbody(sbody.format(**vxx),**kwargs)
        for vxx in odata
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
  projectinfo:
    basename: Hello World Project
    geekname: helloworldproject
  peopletable:
  - fname: Homer
    lname: Simpson
  - fname: Maggie
    lname: Bimpson
  - fname: Lisa
    lname: Dimpson
  ''')
  vout = ''
  vout += str(PyHereDoc()
          .concat("""
            ## Hello: {basename}
            * Hola
            * Hello
            * Bonjour
            ----
            """
            ,data=odata['projectinfo'], puts='>',strip='<>',indent=0)
          .each("""
            * {fname:<12}|{lname}
          """,data=odata['peopletable'],puts='>',strip='<>',dedent=1)
          .concat("""
            ----
            ## World: {basename}
            * Mundo
            * World
            * Monde
            ----
            """
            ,data=odata['projectinfo'], puts='>',strip='<>',indent=0)
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
