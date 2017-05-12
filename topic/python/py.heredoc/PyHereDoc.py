# -*- coding: utf-8 -*-
"""
### <beg-file_info>
### document_metadata:
###   - caption: "__blank__"
###     dmid: "pyheredoc_zigggy07glare"
###     date: created="2017-05-12"
###     last: lastmod="2017-05-12"
###     tags: python,heredoc,template
###     lastupdate: "__lastupdate__"
###     desc: |
###         * base class for python heredoc
###     seealso: |
###         * __seealso__
### <end-file_info>
"""

## begin_ init
if('region::python_init'):
  ## std lib
  import os
  import re
  import string
  import sys
  import textwrap
  import yaml

if('py_init_class'):
  # class FormatExtend(str):
  #   '''
  #   extend python str.format()
  #     * permit custom placeholder delimiters
  #     * support simple loops
  #   '''
  #   def __new__(cls, value, srcdata={}, tkbeg='<%',tkend='%>',):
  #     return str.__new__(cls,value)
  #   def __init__(self,value,srcdata={}, tkbeg='<%',tkend='%>'):
  #     self.srcdata = srcdata;self.tkbeg = tkbeg;self.tkend = tkend;
  #   def tokenize(self): return(self.__str__()
  #     .replace('{','{{').replace('}','}}')
  #     .replace(self.tkbeg,'{').replace(self.tkend,'}'))
  #   def render(self): return(
  #     self.tokenize().format(**self.srcdata))

  class Document(object):
    def __init__(self, strval=None, ddata=None, dconfig=None, ):
      self.strval   = strval    if bool(strval)   else ""
      self.ddata    = ddata     if bool(ddata)    else []
      self.dconfig  = dconfig   if bool(dconfig)  else {}
    ##enddef;;
    def proc_retokenize(self,ssinput=''):
      return(ssinput.__str__()
        .replace('{','{{').replace('}','}}')
        .replace(self.tkbeg,'{').replace(self.tkend,'}')
        )
    ##enddef;;

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
      sputs   = str(kwargs['puts'])   if ('puts'  in kwargs)  else ""
      schomp  = str(kwargs['chomp'])  if ('chomp' in kwargs)  else ""
      snewl   = str(kwargs['n'])      if ('n'     in kwargs)  else ""
      sbody   = str(sbody)            if (not sbody is None)  else ""
      ## kwargs synonym convert
      if (snewl == ''):
        pass
      elif (snewl == '1'):
        sputs = '<'
      elif (snewl == '2'):
        sputs = '>'
      elif (snewl == '3'):
        sputs = '<>'
      ##;;

      ##
      if(bdedent or iindent > -1):  sbody = textwrap.dedent(sbody)
        ## TODO: decide whether you want this
        ## dedent is implicit when indent is present and gt neg1
      ##;;

      ##
      if(sstrip):       sbody = self.fmtstrip(sbody,sstrip)
      if(schomp):       sbody = self.fmtchomp(sbody,schomp)
      if(sputs):        sbody = self.fmtputs(sbody,sputs)
      if(iindent > -1): sbody = self.fmtindent(sbody,iindent)
      return sbody
      ##;;
    ##enddef

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
      sputs       = str(kwargs['puts'])  if ('puts'   in kwargs) else ""
      sstrip      = str(kwargs['strip']) if ('strip'  in kwargs) else ""
      odata       = (kwargs['data'])     if ('data'   in kwargs) else None
      if(False):
        pass
      elif( odata ):
        #self.strval += self.fmtbody(sbody.format(**odata),**kwargs)
        self.strval += self.fmtbody(sbody.format(**odata),**kwargs)
        FormatExtend(sbody,odata).render()
      elif( not odata ):
        #self.strval += self.fmtbody(str(sbody),**kwargs)
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

    def dedent(self):
      self.strval = textwrap.dedent(self.strval)
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
      except Exception, exx:
        pass
      ##
      return self.anonop
    ##;;
