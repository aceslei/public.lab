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

    ### ------------------------------------------------------------------------

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
    age:   33
  - fname: Maggie
    lname: Bimpson
    age:   23
  - fname: Lisa
    lname: Dimpson
    age:   13
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
            * {fname:<12}|{lname:^20}|{age}
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
